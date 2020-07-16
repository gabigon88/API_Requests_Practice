from time import sleep
import requests
import json

goodCode = '7632145' # 商品在MOMOM網的編號

requests.urllib3.disable_warnings() # 關閉requests的警告

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

payload = {
    'hidCaptchaID':'4F87CEDD86FB92C8FA112B0D7E958780-m1.b1-shop24',
    'preUrl':'https://www.momoshop.com.tw/main/Main.jsp',
    'arkDistinctId':'JSfa96d35da9aef962d1b64b95341ba4f1fa96',
    'gflag':'01',
    'memId': '', # 填入MOMOM帳號
    'passwd': '', # 填入MOMOM帳號密碼
}

loginURL = "https://www.momoshop.com.tw/login/LoginStatus.jsp?cid=login&oid=login&ctype=B&mdiv=1000100000-bt_0_003_01"
buyURL = "https://cart.momoshop.com.tw/api/shoppingcart/modify/addGoods"
# URL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=7632145"

# seesion具有保持功能，就類似瀏覽器輸入一次密碼之後，會自動保留cookie
res = requests.get('https://www.momoshop.com.tw', headers=headers, verify=False)
headers['Cookie'] = f'JSESSIONID={res.cookies["JSESSIONID"]}; NSC_MC-xxx.npnptipq.dpn.ux*80={res.cookies["NSC_MC-xxx.npnptipq.dpn.ux*80"]}'

session = requests.Session()
response = session.post(loginURL, headers=headers, data=payload, verify=False)

if response.status_code != 200:
    session.close()
    exit()

payload = {
    "host":"WEB",
    "data":{
        "goShopCartYn":"1",
        "goods":[{
            "goodsCode":goodCode,
            "goodsdtCode":"001",
            "goodsCount":"1",
            "work":"first",
            "recoverYn":"0",
            "addtionalGoods":[],
            "setGoods":[],
            "nsGift":[],
            "applimitBuyYn":"0",
            "applimitBuyfsCode":"",
            "cn":"","defDely":"",
            "limitBuy4MemberYn":"1",
            "limitBuyQty":"5",
            "negativeProfit":"0",
            "promoNo":"",
            "savegetAmt":"",
            "canUseBuy1Get1FreeYn":"0"
        }],
        "cycleTimes":"2",
        "cycleYn":"0",
        "webArea":"",
        "webCategoryCode":"5100100358",
        "webCid":"",
        "webCtype":"",
        "webOid":""
    }
}

response = session.post(buyURL, headers=headers, data=payload, verify=False)
response = session.get('https://www.momoshop.com.tw/servlet/NewCampaignServlet?cart_name=ec10', headers=headers, verify=False)
print(response.text)

session.close()