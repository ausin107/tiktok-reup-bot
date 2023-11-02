from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import pickle, time, os

def get_all_videos_name():
    file_names = []
    for root, dirs, files in os.walk('D:\\mini-project\\tiktok-reup-bot\\videos\\'):
        for file in files:
            file_names.append('D:\\mini-project\\tiktok-reup-bot\\videos\\' + file)
    return file_names  

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options=options)

browser.get("https://www.facebook.com/")
with open("fb_cookies.pickle", "rb") as f:
    cookies = pickle.load(f)
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get("https://www.facebook.com/crazyrelax24h")
change_btn = browser.find_element(By.CLASS_NAME, "xwzsa0r")
change_btn.click()
time.sleep(5)
all_videos_name = get_all_videos_name()
for video in all_videos_name:
    browser.get("https://www.facebook.com/reels/create/?surface=ADDL_PROFILE_PLUS")
    time.sleep(3)
    input_btn = browser.find_element(By.CLASS_NAME, "x1u5z0ei")
    input_btn.click()
    time.sleep(3)
    keyboard = Controller()
    keyboard.type(video)
    keyboard.press(Key.enter)
    time.sleep(3)
    next_btn = browser.find_element(By.CLASS_NAME, "x1fq8qgq")
    next_btn.click()
    next_btn_2 = browser.find_element(By.CSS_SELECTOR, "span.x1s688f.xtk6v10")
    next_btn_2.click()
    time.sleep(3)
    video_title = browser.find_element(By.CLASS_NAME, "notranslate")
    video_title.send_keys("Hahaha #memesontheearth #trending #viral #foryoupage #fyp #meme #funny #tiktok")
    time.sleep(30)
    upload_btn = browser.find_element(By.CSS_SELECTOR, "span.x1s688f.xtk6v10")
    upload_btn.click()
    time.sleep(10)
