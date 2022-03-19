from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

def main():
    try:
        driver = getDriver()
        driver.get(URL)

        config = getConfig()

        naverLogin(driver, config['userId'], config['userPw'])

    except Exception as e:
        print(str(e))
    else:
        print("Main process is done.")
    finally:
        os.system("Pause")
        driver.quit()


def getConfig():
    try:
        with open('config.json') as jsonFile:
            jsonData = json.load(jsonFile)
    except Exception as e:
        print("Error in reading config file, {}".format(e))
        return None
    else:
        return jsonData

def naverLogin(driver, id, pw):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#id"))
    )
    element.send_keys(id)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#pw"))
    )
    element.send_keys(pw)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.btn_global"))
    )
    element.click()

    return False

def getDriver():
    driver = webdriver.Chrome(r'C:\chromedriver.exe')
    driver.implicitly_wait(3)
    return driver

if __name__=='__name__':
    main()

