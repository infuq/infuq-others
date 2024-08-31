import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def i0(driver):
    driver.get("https://www.baidu.cn")
    driver.implicitly_wait(5)

    # 获取元素
    element = driver.find_element(by=By.NAME, value='tj_settingicon')
    ActionChains(driver).move_to_element(element).perform()


if __name__ == '__main__':

    driver = webdriver.Chrome()

    i0(driver)

    time.sleep(5)
    driver.close()

    # 右击
    # context_click()
    # 双击
    # double_click()
    # 拖拽
    # double_and_drop()
    # 悬停
    # move_to_element()
    # 执行
    # perform()




