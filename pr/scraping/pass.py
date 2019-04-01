from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from decouple import config
from unipath import Path
BASE_DIR = Path(__file__).parent
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

pass_login_url = 'https://pass.calpoly.edu/login.do'
pass_url = 'https://pass.calpoly.edu/main.html'

timeout = 5

browser = webdriver.Chrome(executable_path='c:/Gitprojects/pr/chromedriver.exe')
browser.get(pass_login_url)

try:
    submit_button = EC.presence_of_element_located((By.NAME, '_eventId_proceed'))
    WebDriverWait(browser, timeout).until(submit_button)
    print('found button!')
except TimeoutException:
    print('page timed out.')

username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys(config('LOGIN_USERNAME'))
password.send_keys(config('LOGIN_PASSWORD'))
browser.find_element_by_name('_eventId_proceed').click()
browser.find_element_by_id('dismissNew').click()
# filter_box = browser.find_element_by_id('filterbox-list-view')
department_list = browser.find_element_by_xpath("//select[@data-filter='dept']")
majors = department_list.find_elements_by_tag_name('option')
for major in majors:
    split = major.text.split('-')
    abbv = split[0]
    pre_major = split[1].split(' ')
    for i, word in enumerate(pre_major):
        if word != 'and':
            pre_major[i] = word.capitalize()
    pre_major = ' '.join(pre_major)
    print(abbv)
    print(pre_major)