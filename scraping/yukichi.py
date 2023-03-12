from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def main(url):
    path = "/Applications/chromedriver"
    driver = webdriver.Chrome(executable_path=path)

    driver.get(url)

    img = driver.find_element(By.XPATH, '')  # ここは穴埋め！
    src = img.get_attribute('src')
    if src:
        # ファイルの保存
        with open(f'yukichi.png', 'wb') as f:
            f.write(img.screenshot_as_png)
    driver.quit()


if __name__ == '__main__':
    url = 'https://ja.wikipedia.org/wiki/%E7%A6%8F%E6%BE%A4%E8%AB%AD%E5%90%89'
    main(url)
