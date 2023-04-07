from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд) - method - text_to_be_present_in_element
# selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(locator, text_)
# говорим Selenium проверять в течение 12 секунд, пока текст у элемента с id = price не станет равным $100
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
# Нажать на кнопку "Book"
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# Решить математическую задачу
# Считать значение для переменной x:
x_element = browser.find_element(By.ID, "input_value")
    # Взять у этого элемента значение атрибута input_value, которое является значением x для задачи
x = x_element.text
     # Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
    # Ввести ответ в текстовое поле
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
    
    #Нажать на кнопку Submit
button = browser.find_element(By.ID, "solve")
button.click()


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()
