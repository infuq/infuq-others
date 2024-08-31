import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def i0(driver):
    driver.get("http://cp-test.pinpinding.com/")
    driver.implicitly_wait(5)

    # 输入账号
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    username.send_keys("sun111")
    password.send_keys("123456")

    # 等待弹框出现
    WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='系统发布通告']/div[3]/span/div/button")))

    # 点击弹框
    alert_notice = driver.find_element(By.XPATH, "//div[@aria-label='系统发布通告']/div[3]/span/div/button")
    alert_notice.click()

    time.sleep(1)

    # 系统登录
    btn_login = driver.find_element(By.CSS_SELECTOR, "button.loginbtn")
    btn_login.click()

    WebDriverWait(driver, 30, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.no-redirect.last")))

    print(driver.page_source)





if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    # options.add_argument('--headless')  # 无头模式
    # 设置为开发者模式, 防止被各大网站识别出来使用了Selenium
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options=options)

    i0(driver)

    time.sleep(5)
    driver.close()

