from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # 设置浏览器大小
    # driver.maximize_window()
    # driver.set_window_size(1500, 1500)

    driver.get("https://www.infuq.com")

    # 网页标题
    print(driver.title)
    # 当前网址
    print(driver.current_url)
    # 浏览器名称
    print(driver.name)
    # 网页源码
    print(driver.page_source)

    time.sleep(5)

    driver.get("https://www.bilibili.com")

    # 获取元素
    element = driver.find_element(by=By.CLASS_NAME, value='channel-link')


    time.sleep(5)

    # 后退
    # driver.back()
    # 前进
    # driver.forward()
    # 刷新
    driver.refresh()


    driver.close()
