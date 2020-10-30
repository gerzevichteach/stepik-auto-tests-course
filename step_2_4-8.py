from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time, math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # ожидаем ранее скрытые элементы
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 15 секунд, пока цена на станет $100
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    # Кликаем на кнопку "Book"
    browser.find_element_by_id("book").click()
    # Появляется ранее скрытая капча
    # решаем капчу для роботов

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(int(x))
    # Скроллим поле для ввода капчи
    answer = browser.find_element_by_css_selector('#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y) # Вводим капчу
    
    # Скроллим кнопку ввода
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Ожидаем кликабельность кнопки
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    
    button.click()
    
    




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()