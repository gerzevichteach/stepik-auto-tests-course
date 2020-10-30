from selenium import webdriver
import time
import math

try:
  
    link = 'http://suninjuly.github.io/wait1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Нажимаем на кнопку
    browser.find_element_by_id("verify").click()
    
       
    message = browser.find_element_by_css_selector('#verify_message')
    
    assert "successful" in message.text

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
