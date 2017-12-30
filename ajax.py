import requests
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1", cell_overwrite_ok=True)
sheet1.write(0, 0, "fa-name")
sheet1.write(0, 1, "en-name")
sheet1.write(0, 2, "img-link")
sheet1.write(0, 3, "price")
sheet1.write(0, 4, "old-price")
row = 0

r = requests.get('https://rc.digikala.com/fatLatestItems/315669351848385857?howMany=50&withoutBasket=1')
items = r.json()
for i in range(len(items)):
    row = i + 1
    enName = items[i]["zoom_image"].split("/")[-1][:-4]
    sheet1.write(row, 0, items[i]["title"])
    sheet1.write(row, 1, enName)
    sheet1.write(row, 2, items[i]["zoom_image"])
    sheet1.write(row, 3, items[i]["price"])
    sheet1.write(row, 4, items[i]["msrp"])

row += 2
r = requests.get('https://recommender.scarabresearch.com/merchants/123DB8D9C'
                 'CA58C7C/?pv=1708072305&f=f%3APERSONAL%2Cl%3A20%2Co%3A0&cp='
                 '1&vi=559DD4B342548E36&p=162715%7C1509028083&error=%5B%7B%2'
                 '2t%22%3A%22MULTIPLE_CALL%22%2C%22c%22%3A%22go%22%2C%22m%22'
                 '%3A%22Multiple%20calls%20of%20go%20command%22%7D%5D')
responses = r.json()["products"]
for k, v in responses.items():
    sheet1.write(row, 0, v[1])
    enName = v[8].split("/")[-1][:-4]
    sheet1.write(row, 1, enName)
    sheet1.write(row, 2, v[9])
    sheet1.write(row, 3, v[4])
    sheet1.write(row, 4, v[6])
    row += 1


row += 1
r = requests.get(
    'https://search.digikala.com/api2/Data/Get?categoryId=0&ip=0&forPromotionCenter=true&incredibleOnly=true')
items = r.json()["responses"][0]["hits"]["hits"]
for item in items:
    oldPrice = float(item["_source"]["Price"])
    price = oldPrice - float(item["_source"]["Discount"])
    sheet1.write(row, 0, item["_source"]["FaTitle"])
    sheet1.write(row, 1, item["_source"]["EnTitle"])
    sheet1.write(row, 2, item["_source"]["ProductImagePath"])
    sheet1.write(row, 3, price)
    sheet1.write(row, 4, oldPrice)
    row += 1

row += 1
r = requests.get('https://recommender.scarabresearch.com/merchants/123DB8D9CCA58C7C/?'
                 'pv=949653850&xp=1&f=f%3AHOME_1%2Cl%3A20%2Co%3A0%7Cf%3AHOME_2%2Cl%3A'
                 '20%2Co%3A0%7Cf%3AHOME_3%2Cl%3A20%2Co%3A0&cv=1&ca=&cp=1&vi=559DD4B34'
                 '2548E36&p=162715%7C1509028083')
responses = r.json()["products"]
for k, v in responses.items():
    sheet1.write(row, 0, v[1])
    enName = v[8].split("/")[-1][:-4]
    sheet1.write(row, 1, enName)
    sheet1.write(row, 2, v[8])
    sheet1.write(row, 3, v[4])
    sheet1.write(row, 4, v[6])
    row += 1

row += 1
r = requests.get('https://search.digikala.com/api/SearchApi/?sortby=1&status=2&pageno=0&pageSize=15')
items = r.json()["hits"]["hits"]
for item in items:
    sheet1.write(row, 0, item["_source"]["FaTitle"])
    sheet1.write(row, 1, item["_source"]["EnTitle"])
    sheet1.write(row, 2, item["_source"]["ImagePath"])
    sheet1.write(row, 3, item["_source"]["MaxPrice"])
    sheet1.write(row, 4, item["_source"]["MinPriceList"])
    row += 1

book.save("DigikalaAjaxData.xls")
