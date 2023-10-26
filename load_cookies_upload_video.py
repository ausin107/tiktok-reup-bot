from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import pickle, time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get("https://www.facebook.com/")
with open("fb_cookies.pickle", "rb") as f:
    cookies = pickle.load(f)
for cookie in cookies: 
    browser.add_cookie(cookie)
browser.get("https://www.facebook.com/crazyrelax24h")
change_btn = browser.find_element(By.CLASS_NAME, "xwzsa0r")
change_btn.click()
browser.get("https://www.facebook.com/reels/create/?surface=ADDL_PROFILE_PLUS")
time.sleep(3)
input_btn = browser.find_element(By.CLASS_NAME, "x1u5z0ei")
input_btn.click()
time.sleep(3)
keyboard = Controller()
keyboard.type("D:\\mini-project\\tiktok-reup-bot\\videos\\0.mp4")
keyboard.press(Key.enter)
time.sleep(3)
next_btn = browser.find_element(By.CLASS_NAME, "x1fq8qgq")
next_btn.click()
next_btn_2 = browser.find_element(By.CSS_SELECTOR, "span.x1s688f.xtk6v10")
next_btn_2.click()
time.sleep(3)
video_title = browser.find_element(By.CLASS_NAME, "notranslate")
video_title.send_keys("Hahaha #comedy #reelfb #funny")
time.sleep(5)
upload_btn = browser.find_element(By.CSS_SELECTOR, "span.x1s688f.xtk6v10")
upload_btn.click()
