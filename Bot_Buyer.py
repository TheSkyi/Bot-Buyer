from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

homePage = "https://www.bestbuy.com/"
loginPage = "https://www.bestbuy.com/login"
gpuPage = "https://www.bestbuy.com/site/gpu/6505083.p"

driver.get(homePage)

try:
    logoutButton = driver.find_element(By.ID, "logout-button")

except:
    print("User Not Logged In")

    driver.get(loginPage)

    time.sleep(1)

    e_val = "Email"
    p_val = "Password@"

    driver.find_element(By.ID, "fld-e").send_keys(e_val)
    driver.find_element(By.ID, "fld-p1").send_keys(p_val)

    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[4]/button").click()

    time.sleep(2)

driver.get(gpuPage)

while True:
    continue
