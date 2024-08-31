from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get("https://www.infuq.com")
    driver.implicitly_wait(5)

    # 获取元素
    element = driver.find_element(by=By.CLASS_NAME, value='channel-link')


    # 获取元素属性
    element.get_attribute("img")
    element.get_attribute("innerHTML")
    element.get_attribute("outerHTML")

    # 获取输入框里面的内容
    element.get_attribute("value")
    # 
    element.text

    element.get_attribute("innerText")
    element.get_attribute("textContent")

    driver.close()
