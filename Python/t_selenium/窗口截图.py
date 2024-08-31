import time

from selenium import webdriver


def i0(driver):
    driver.get("https://www.baidu.cn")
    driver.implicitly_wait(5)

    driver.get_screenshot_as_file("D:\\baidu_img.png")


if __name__ == '__main__':

    driver = webdriver.Chrome()

    i0(driver)

    time.sleep(5)
    driver.close()


