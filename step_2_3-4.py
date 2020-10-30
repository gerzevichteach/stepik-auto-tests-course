from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
  
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажимаем на кнопку
    browser.find_element_by_css_selector("button.btn").click()
    # Принимаем confirm
    browser.switch_to.alert.accept()
    # на следующей странице
    # решаем капчу для роботов
    x = browser.find_element_by_css_selector('#input_value').text
    
    y = calc(x)
    
    browser.find_element_by_css_selector('#answer').send_keys(y)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
