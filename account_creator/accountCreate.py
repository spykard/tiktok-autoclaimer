import configparser
import time
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from fake_useragent import UserAgent


''' Run Main Function '''
print(f"Starting...")

# Config Parsing
config = configparser.ConfigParser()
config.read('config/config.ini')

# Initiate Selenium Driver
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile, executable_path='.\geckodriver.exe')

driver.get('https://www.tiktok.com/signup?lang=en')
time.sleep(1)

# Start the process of clicking on a series of Buttons on the Website
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ("//*[contains(text(), 'Twitter')]")))).click()

driver.refresh()  # Required

driver.switch_to.window(driver.window_handles[1])  # Switch to 2nd Window
print(f"Loading {driver.current_url}...")

# Bypass both Captcha and Phone check by utilizing Twitter sign up
print(f"Loging in to a Twitter Account... Using the Twitter sign up method bypasses the captcha check. Removing mobile number from Twitter also bypasses the phone check.")
username_twitter = config['Settings']['username_twitter']
element_popup_twitter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username_or_email')))
element_popup_twitter.send_keys(username_twitter)

password_twitter = config['Settings']['password_twitter']
element_popup_twitter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
element_popup_twitter.send_keys(password_twitter)

driver.find_element_by_id('allow').click()

driver.switch_to.window(driver.window_handles[0])  # Switch back to 1st Window
driver.find_element_by_xpath("//*[contains(text(), 'Twitter')]").click()

# Age Gate
element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'select-container-2Ubyt')))  

element[0].click()
driver.find_elements_by_class_name('list-item-MOAq4')[1].click()  # February

element[1].click()
driver.find_elements_by_class_name('list-item-MOAq4')[3].click()  # 4th

element[2].click()
driver.find_elements_by_class_name('list-item-MOAq4')[21].click()  # 1999

driver.find_element_by_class_name('login-button-31D24').click()

# Username Selection (Account has already been created when this page Loads)
username_tiktok = config['Settings']['username_tiktok']
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
element.clear()
element.send_keys(username_tiktok)

# Final Click
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-button-31D24'))).click() 
