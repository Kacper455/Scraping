from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path=r'C:\Users\Admin\PycharmProjects\PythonProject1\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.miejski.pl/slowo-Historia+z+J%C4%99drzychowa')
wait = WebDriverWait(driver, 10)

try:
    find = driver.find_element(By.XPATH, "//span[@class='vote up']")
    driver.refresh()
    find.click()
    print("Pomyślnie kliknięto")

    time.sleep(3)

    driver.quit()
except:
    while True:
        example = driver.find_element(By.XPATH, ('//*[@id="actions"]/a[1]')).click()

        find = driver.find_element(By.XPATH, "//span[@class='vote down']")

        find.click()

        time.sleep(5)

input("Press enter to continue...")