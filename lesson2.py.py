from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)
    button = browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
         return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
