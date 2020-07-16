import requests
import json

requests.urllib3.disable_warnings() # 關閉requests的警告
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

# get product ID
url = 'https://rtapi.ruten.com.tw/api/search/v3/index.php/core/prod'
my_params = {
    'q':'switch 主機',
    'type':'direct',
    'sort':'rnk/dc',
    'offset':'1',
    'limit':'50'
}
r = requests.get(url, verify=False, headers = header, params = my_params)
tempDict = json.loads(r.text)
productIDList = []
for item in tempDict['Rows']:
    productIDList.append(item['Id'])
productIDStr = ','.join(productIDList)

# use product ID to get info
url2 = f'https://rtapi.ruten.com.tw/api/prod/v2/index.php/prod?id={productIDStr}'
r = requests.get(url2, verify=False, headers = header)
tempDict = json.loads(r.text)
i = 1
for item in tempDict:
    print(f"{i}.{item['ProdName']}\n價錢：{item['PriceRange']}\n圖片：https://c.rimg.com.tw{item['Image']}")
    i = i + 1