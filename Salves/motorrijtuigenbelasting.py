import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = 'https://www.belastingdienst.nl/wps/wcm/connect/nl/auto-en-vervoer/content/hulpmiddel-motorrijtuigenbelasting-berekenen'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path="chromedriver",
                            options=options)
driver.set_window_size(1200, 860)

# Send a get request to the url

t1 = 1
t2 = 1

url = 'https://www.belastingdienst.nl/wps/wcm/connect/nl/auto-en-vervoer/content/hulpmiddel-motorrijtuigenbelasting-berekenen'
driver.get(url)

time.sleep(t1)

driver.find_element(By.XPATH, '//*[@id="divV1-1"]/div/div[1]/label').click()
print('Woont u in Nederland? Clicked [Ja]')

time.sleep(t2)

Select(driver.find_element(By.ID, 'V1-2')).select_by_visible_text('Personenauto')
print('Soort Moterrijtuig - Selected [Personenauto]')

time.sleep(t2)

driver.find_element(By.XPATH, '//*[@id="divV1-16"]/div/div[2]/label').click()
print('Elektrisch? Clicked [Nee]')

time.sleep(t2)

Select(driver.find_element(By.ID, 'V1-5')).select_by_visible_text('Drenthe')
print('Provincie - Selected [Drenthe]')

time.sleep(t2)

Select(driver.find_element(By.ID, 'V1-7')).select_by_visible_text('Diesel')
print('Brandstof - Selected [Diesel]')

time.sleep(t2)

driver.find_element(By.XPATH, '//*[@id="divV1-18"]/div[2]/div[2]/label').click()
print('Fijnstoftoeslag? Clicked [Nee]')

time.sleep(t2)

Select(driver.find_element(By.ID, 'V1-9')).select_by_visible_text('1051 t/m 1150')
print('Gewichtsklasse - Selected [1051 t/m 1150]')

time.sleep(t2)

driver.find_element(By.ID, "butResults").click()

time.sleep(10)
driver.quit()
print("Done")