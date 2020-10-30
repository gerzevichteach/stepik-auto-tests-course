from selenium import webdriver
import time, math, os


try:
    name_file = '2_2_8.txt'
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, name_file)
    
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    # заполняем поле имя 
    browser.find_element_by_css_selector("input[name = 'firstname']").send_keys("Виктор")
    
    # заполняем поле фамилия
    browser.find_element_by_css_selector("input[name = 'lastname']").send_keys("Семенов")
    
    # заполняем поле почта
    browser.find_element_by_css_selector("input[name = 'email']").send_keys("gerzevich@yandex.ru")
    
    # заполняем поле почта
    browser.find_element_by_css_selector("input[name = 'file']").send_keys(file_path)
    
    # Нажимаем на кнопку "Submit"
    browser.find_element_by_tag_name("button").click()
    
        
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
