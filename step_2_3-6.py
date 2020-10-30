from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
  
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажимаем на кнопку
    browser.find_element_by_css_selector("button.btn").click()
    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # на следующей странице
    
    time.sleep(2)
    # решаем капчу для роботов
    
    x = browser.find_element_by_css_selector('#input_value').text
    
    y = calc(int(x))
    
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
