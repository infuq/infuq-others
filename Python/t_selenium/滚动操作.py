import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def bottom(driver):
    temp_height = 0
    x = 1000
    y = 1000
    while True:
        js = "var q=document.getElementsByClassName('cdk-virtual-scroll-viewport')[0].scrollTop={}".format(x)
        driver.excute_script(js)
        time.sleep(0.5)
        x += y
        check_height = driver.excute_script(
            "return document.getElementsByClassName('cdk-virtual-scroll-viewport')[0].scrollTop;")
        if check_height == temp_height:
            break
        temp_height = check_height


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get("https://www.bilibili.com")
    driver.implicitly_wait(5)

    # 获取元素
    element = driver.find_element(by=By.CLASS_NAME, value='channel-link')
    bottom(driver)
    time.sleep(7)

    driver.close()
