from selenium import webdriver
import time

try:
  
    link = 'http://suninjuly.github.io/wait1.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
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
