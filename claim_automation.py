# Current version 0.0.5
# Подключаем библиотеки
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Переменные
Adres = "г. Саратов, ул. Чернышевского, 189"  # Адрес точки которую мы ищем
path_driver = r"D:\Git\claim_automation\chromedriver.exe"  # Путь до драйвера хрома

Cause = 1
if Cause == 1:
    Purchase_returns = "ВОЗВРАТЫ"
else:
    Purchase_returns = "ПРЕТЕНЗИИ"

browser = webdriver.Chrome(executable_path=path_driver)
browser.implicitly_wait(30)
Login = "Тут логин"
Password = "А тут пароль"
wait = WebDriverWait(browser, 30)


# Функции
def find_and_click(by, pointer):
    time.sleep(3)
    Element = by(pointer)
    Element.click()


def find_and_text_input(text, by, pointer):
    time.sleep(3)
    Element = by(pointer)
    Element.send_keys(text)
    Element.send_keys(Keys.ENTER)


# Открываем браузер, разворачиваем на весь экран, и переходим по ссылке
browser.maximize_window()
browser.get('тут адрес страницы куда надо конектиться')

# Проверяем что заговолов странице содержит [Катрен | Личный кабинет клиента]
assert "Катрен | Личный кабинет клиента" in browser.title

# Авторизация.
field_login = browser.find_element_by_id("login")
field_pass = browser.find_element_by_id("password")
field_login.send_keys(Login)
field_pass.send_keys(Password)
field_pass.send_keys(Keys.ENTER)

# Вводим адрес точки в поисковую страку и нажимаем ENTER.
find_and_text_input(Adres, browser.find_element_by_xpath,
                 "/html/body/ui-view[1]/user-layout/ui-view[1]/header/div[2]/div/div[2]/autodests/div/div[1]/div["
                 "2]/form/div[1]/input")

# Разворачивем юр лицо и кликаем на адрес точки
find_and_click(browser.find_element_by_xpath,
            "/html/body/ui-view[1]/user-layout/ui-view[1]/header/div[2]/div/div[2]/autodests/div/div["
             "2]/div/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/span")


find_and_click(browser.find_element_by_xpath,
             "/html/body/ui-view[1]/user-layout/ui-view[1]/header/div[2]/div/div[2]/autodests/div/div["
             "2]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]")

# Выбираем тип возврата (претензия или возврат) из верхнего меню
browser.find_element_by_partial_link_text(Purchase_returns).click()

# Нажимаем кнопку создать притензию или возврат соответственно
find_and_click(browser.find_element_by_xpath,
             "/html/body/ui-view[1]/user-layout/ui-view[1]/header/div[3]/div/div/div[2]/div/div[2]/span")

# Закрытие браузера если все выполнено.
time.sleep(5)
browser.quit()
