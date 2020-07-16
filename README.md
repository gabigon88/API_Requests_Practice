# API_Requests_Practice
用電商網站的API 練習發起Requests請求  

檔案1  
>RuTen_API_requests.py

網路上Requests教學的文章是用蝦皮當對象  
自己看完後，要練習Requests就找了露天當測試  
沒想到露天的資料庫API蠻特別的  
他們家API拆成兩段，第一個段search API只搜尋商品在資料庫裡的ID  
拿到商品在資料庫裡的ID後，第二段才是用那些ID，取得商品的各項資訊(商品名、價錢等等)  

檔案2  
>MOMO_webdriver.py

今年大家在搶PS4搖桿造型悠遊卡時寫的Selenium自動化程式  
以Selenium的執行速度，就算使用headless模式應該也是搶不到  
不過後來MOMO整個網路塞爆了，所以根本也沒用XD  
此檔案跟Requests練習沒什麼關係  
只是成為後面突發奇想 檔案3 的契機  

檔案3  
>MOMO_API_requests.py

前面有提到，理論上Selenium的執行速度就算自動化了  
應該還是搶不贏專業黃牛的搶購  
後來就突然想到那如果直接Requests發請求應該就是最快的辦法了  
所以寫了這隻程式就誕生了~  
但實作上登入的POST requests都一直無法成功  
因為用瀏覽器F12 監看  
發現登入的payloadr裡有一項資料叫hidCaptchaID
推測是登入時有隱藏的驗證碼  
但MOMO不想要讓使用者輸入麻煩  
自己用js之類的在背景把他解掉了  
目前還是無法正確登入QQ  