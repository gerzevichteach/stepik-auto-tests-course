from selenium import webdriver
import time

try:
  
    link = 'http://suninjuly.github.io/cats.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    #Нажимаем на кнопку
    browser.find_element_by_id("button")
    
       
   
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
