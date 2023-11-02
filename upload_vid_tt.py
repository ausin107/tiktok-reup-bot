from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time,pickle, os, shutil, re

def get_all_videos_name():
    file_names = []
    for root, dirs, files in os.walk('D:\\douyinVideo\\cooking\\'):
        for file in files:
            file_names.append('D:\\douyinVideo\\cooking\\' + file)
    return file_names 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options = options)
browser.get("https://www.tiktok.com/")
with open("tt_cookies.pickle", "rb") as f:
    cookies = pickle.load(f)
for cookie in cookies:
    browser.add_cookie(cookie)
time.sleep(2)
allVideos = get_all_videos_name()
for video in allVideos:
    browser.get("https://www.tiktok.com/creator-center/upload?from=upload")
    time.sleep(5)
    iframe = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/iframe')
    browser.switch_to.frame(iframe)
    upload_btn = browser.find_element(By.CLASS_NAME, "before-upload-stage")
    upload_btn.click()
    time.sleep(3)
    keyboard = Controller()
    keyboard.type(video)
    keyboard.press(Key.enter)
    time.sleep(5)
    video_caption = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div')
    video_caption.clear()
    video_caption.send_keys("#xuhuong #tiktok #fyp #viral #cooking #dailycookingmama")
    time.sleep(20)
    post_btn = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[8]/div[2]/button')
    post_btn.click()
    browser.switch_to.default_content()
    browser.get("https://www.tiktok.com/creator-center/upload?from=upload")
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)
    currentVideo = re.findall(r'\d+', video)
    shutil.move(video, f"D:\\douyinVideo\\completed\\{currentVideo[0]}.mp4")