from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def main(url):
    path = "/Applications/chromedriver"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=path,options=options)
    driver.get(url)

    img = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]/td/a/img')#ここは穴埋め！
    src = img.get_attribute('src')
    if src:
        # ファイルの保存
        with open(f'yukichi.png', 'wb') as f:
            f.write(img.screenshot_as_png)
    driver.quit()

if __name__=='__main__':
    url = 'https://ja.wikipedia.org/wiki/%E7%A6%8F%E6%BE%A4%E8%AB%AD%E5%90%89'
    main(url)