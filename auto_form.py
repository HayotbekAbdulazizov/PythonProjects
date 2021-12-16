from selenium import webdriver
import time
from selenium.webdriver.common.by import By

print(' In Web')
web = webdriver.Firefox()
# web.get('https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet')
# web.get('https://www.instagram.com/accounts/login/?next=%2Flogin%2F&source=desktop_nav')
web.get('https://robocode.uz')

print(' Got instagram')

time.sleep(3)
print(' got username input ')

# username_input = web.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
# username_input = web.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
# username_input.send_keys('hayotbekabdulazizov200')1111

# password_input = web.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
# password_input = web.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
# password_input.send_keys('gafur22abdulazizov')

# submit = web.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
# submit  = web.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
# submit.click()

captch  = web.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
print('found')

# confirmation_text = web.find_element_by_css_selector('#slfErrorAlert')
time.sleep(0.7)
# confirmation_text = web.find_element(By.CSS_SELECTOR, '')
# print(confirmation_text.text)
