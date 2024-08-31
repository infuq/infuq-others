import time

from selenium import webdriver


def i0(driver):
    driver.get("https://www.baidu.cn")
    driver.implicitly_wait(5)

    js = "window.scrollTo(100,450);"
    driver.execute_script(js)  # 通过javascript设置浏览器窗口的滚动条位置


if __name__ == '__main__':

    driver = webdriver.Chrome()

    i0(driver)

    time.sleep(5)
    driver.close()


