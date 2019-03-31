from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

pass_login_url = 'https://pass.calpoly.edu/login.do'
pass_url = 'https://pass.calpoly.edu/main.html'

timeout = 5


browser = webdriver.Chrome(executable_path='E:/Gitprojects/pr/chromedriver.exe')
browser.get(pass_login_url)

try:
    submit_button = EC.presence_of_element_located((By.NAME, '_eventId_proceed'))
    WebDriverWait(browser, timeout).until(submit_button)
    print('found button!')
except TimeoutException:
    print('page timed out.')
# browser.find_element_by_id('dismissNew').click()

username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')

username.send_keys('')
password.send_keys('')
browser.find_element_by_name('_eventId_proceed').click()
