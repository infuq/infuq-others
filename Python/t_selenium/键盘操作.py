from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get("https://www.infuq.com")

    # 获取元素
    element = driver.find_element(by=By.CLASS_NAME, value='channel-link')

    # 删除键
    # send_keys(Keys.BACK_SPACE)
    # 空格键
    # send_keys(Keys.SPACE)
    # 制表键
    # send_keys(Keys.TAB)
    # 回退键
    # send_keys(Keys.ESCAPE)
    # 回车
    # send_keys(Keys.ENTER)
    # 全选
    # send_keys(Keys.CONTRL,‘a’)
    # 复制
    # send_keys(Keys.CONTRL,‘c’)
    # 剪切
    # send_keys(Keys.CONTRL,‘x’)
    # 粘贴
    # send_keys(Keys.CONTRL,‘x’)
    # 键盘F1
    # send_keys(Keys.F1)



    driver.close()
