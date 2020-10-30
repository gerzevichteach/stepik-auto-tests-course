from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:  
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    # Ищем значение х
    x = int(browser.find_element_by_css_selector('#input_value').text)
    # считаем
    z = calc(x)
    # вставляем в видимое поле #answer    
    browser.find_element_by_css_selector("#answer").send_keys(z)
    
    # Выбраем checkbox "I'm the robot"
    browser.find_element_by_css_selector('#robotCheckbox').click()
    
    # Скроллим до Переключателя radiobutton "Robots rule!"
    robotRule = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
    
    # Переключаем radiobutton "Robots rule!"
    browser.find_element_by_css_selector('#robotsRule').click()
    
    # Скроллим до  кнопки "Submit"
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Нажимаем на кнопку "Submit"
    button.click()
    
        
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
