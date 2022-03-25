from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

#input 데이터를 pyperclip 이용해 copy & paste하여 xpath로 전달
def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click() #Please use find_element(by=By.XPATH, value=xpath) instead
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

#id, password
#Warning! private information
id = '****'
pw = '*********'
#크롬 드라이버 열기
driver = webdriver.Chrome('c:\chromedriver.exe')
driver.implicitly_wait(3)

#url 열기
URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(URL)

#id, password copy_input 함수통해 copy & paste
copy_input('//*[@id="id"]', id)
time.sleep(1)
copy_input('//*[@id="pw"]', pw)
time.sleep(1)

#로그인 버튼 클릭
driver.find_element_by_xpath('//*[@id="log.login"]').click()

#Test1
#Test2
#Test3
#git account Last Test

