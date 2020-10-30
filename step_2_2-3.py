from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
  
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля #input_value
    x = browser.find_element_by_css_selector('#num1').text
    y = browser.find_element_by_css_selector('#num2').text
    z = int(x) + int(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(z)) # ищем элемент с текстом
#    browser.find_element_by_tag_name("select").click()
#    browser.find_element_by_css_selector('[value= "' + str(z) + '"]').click()

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
