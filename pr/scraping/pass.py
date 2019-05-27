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

poly_portal = 'https://myportal.calpoly.edu/f/u17l1s6/normal/render.uP'
student_center = 'https://cmsweb.calpoly.edu/psp/CSLOPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL'

timeout = 5

browser = webdriver.Chrome(executable_path='c:/Gitprojects/pr/chromedriver.exe')
browser.get(poly_portal)

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
student_center_tag = browser.find_element_by_xpath("//a[@class='singleclick-link'][3]")
student_center_tag.click()
# Switch tabs
browser.switch_to_window(browser.window_handles[1])
page_container_table = browser.find_element_by_tag_name('body')
print(page_container_table.get_attribute('innerHTML'))
# try:
#     enroll_link = EC.presence_of_element_located((By.ID, 'DERIVED_SSS_SCR_SSS_LINK_ANCHOR2'))
#     WebDriverWait(browser, timeout).until(enroll_link)
#     print('enroll found.')
# except TimeoutException:
#     print('could not find enroll link.')
    
# print(clicky_boi.text)
# student_center_link = student_center_tag.get_attribute('href')
# browser.find_element_by_id('dismissNew').click()
# # filter_box = browser.find_element_by_id('filterbox-list-view')
# department_list = browser.find_element_by_xpath("//select[@data-filter='dept']")
# majors = department_list.find_elements_by_tag_name('option')
# for major in majors:
#     split = major.text.split('-')
#     abbv = split[0]
#     pre_major = split[1].split(' ')
#     for i, word in enumerate(pre_major):
#         if word != 'and':
#             pre_major[i] = word.capitalize()
#     pre_major = ' '.join(pre_major)
#     print(abbv)
#     print(pre_major)