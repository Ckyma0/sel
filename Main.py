#Импортируем модули
import requests #Модуль запросов
from selenium import webdriver #Модуль Selenium драйвера
from selenium.webdriver.chrome.service import Service #Модуль Selenium драйвера
import time #Модуль ожидания или сна

#Указываем айди профиля в антике
profile_id = '1111111'

#Делаем запрос к антику и вызываем нужный профиль
mla_url = 'http://localhost:3001/v1.0/browser_profiles/'+profile_id+'/start?automation=1'
resp = requests.get(mla_url)

#Получаем ответ после запуска профиля
json = resp.json()
print(json)

#Парсим значение открытого порта профиля антика
port = str(json['automation']['port'])
print(port)

#Инициализируем путь к веб драйверу Dolphin Anti
chrome_dolphin_driver_path = Service("C:/Users/duglas/Desktop/SELENIUM/chromedriver")

#Загружаем предварительные настройки в Selenium драйвер и подключаемся к порту запущенного профиля
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:"+port
driver = webdriver.Chrome(service=chrome_dolphin_driver_path, chrome_options=options)

#Загружаем страницы в ранее открытом профиле и автоматизируем любые действия
try:
    driver.get('https://google.com/')
    print(driver.title)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()