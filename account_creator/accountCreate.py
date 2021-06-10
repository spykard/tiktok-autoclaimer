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

username_twitter = config['Settings']['username_twitter']
element_popup_twitter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username_or_email')))
element_popup_twitter.send_keys(username_twitter)

password_twitter = config['Settings']['password_twitter']
element_popup_twitter = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
element_popup_twitter.send_keys(password_twitter)

driver.find_element_by_id('allow').click()

driver.switch_to.window(driver.window_handles[0])  # Switch back to 1st Window
driver.find_element_by_xpath("//*[contains(text(), 'Twitter')]").click()



quit()

# Bypass both Captcha and Phone check by utilizing Twitter sign up
print(f"Loging in to a Twitter Account... Using the Twitter sign up method bypasses the captcha check. Removing mobile number from Twitter also bypasses the phone check.")

quit()

#Fill the email value
email_field = driver.find_element_by_name('emailOrPhone')
fake_email = email.getFakeMail()
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
# Fill username value
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)
# Fill password value
password_field = driver.find_element_by_name('password')
password_field.send_keys(account.generatePassword())  # You can determine another password here.
print(account.generatePassword())
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

time.sleep(8)

#Birthday verification
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
time.sleep(3)
#
fMail = fake_email[0].split("@")
mailName = fMail[0]
domain = fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)
try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if(not_valid.text == 'That code isn\'t valid. You can request a new one.'):
      time.sleep(1)
      driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
      time.sleep(10)
      instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
      confInput = driver.find_element_by_name('email_confirmation_code')
      confInput.send_keys(Keys.CONTROL + "a")
      confInput.send_keys(Keys.DELETE)
      confInput.send_keys(instCodeNew, Keys.ENTER)
except:
      pass
