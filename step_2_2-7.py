from selenium import webdriver
import time, math, os


try:
    name_file = '2_2_8.txt'
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, name_file)
    with open (file_path) as f:
        for l in f:
            print(l)
    
    
        
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    
