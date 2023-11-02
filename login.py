from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle
import json
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options=options)
browser.get("https://www.facebook.com/")

with open("account.json", "r") as f:
    data = json.load(f)
account_input = browser.find_element(By.ID, "email")
account_input.send_keys(data["gmail"])
password_input = browser.find_element(By.ID, "pass")
password_input.send_keys(data["password"])
login_btn = browser.find_element(By.NAME, "login")
login_btn.click()
time.sleep(10)
cookies = browser.get_cookies()
with open("fb_cookies.pickle", "wb") as f:
    pickle.dump(cookies, f)
browser.close()

