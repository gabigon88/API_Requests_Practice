from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

account = '' # 填入MOMOM帳號
password = '' # 填入MOMOM帳號密碼

URL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=7632145" # 要購買的商品網址

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get(URL)

while driver.current_url != URL:
    driver.get(URL)

wait.until(EC.presence_of_element_located((By.ID,"LOGINSTATUS"))).click()
wait.until(EC.presence_of_element_located((By.ID,"memId"))).send_keys(account)
pwTF = wait.until(EC.presence_of_element_located((By.ID,"passwd_show")))
ActionChains(driver).move_to_element(pwTF).click(pwTF).perform()
wait.until(EC.presence_of_element_located((By.ID,"passwd"))).send_keys(password)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/dl[2]/dd[6]/input'))).click()

flag = True
buyBtn = None
while flag:
    try:
        buyBtn = driver.find_element_by_xpath('//*[@id="buy_yes"]/a/img')
    except:
        driver.refresh()
    
    if buyBtn is not None:
        flag = False

buyBtn.click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="shpSumm"]/div/ul/li[1]/a'))).click()
wait.until(EC.presence_of_element_located((By.ID,"orderSave"))).click()
driver.quit()