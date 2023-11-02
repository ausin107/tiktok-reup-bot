from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests, time, json

#sstik downloader ann curlconverter to download video from tiktok
def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")

    cookies = {
        '_gid': 'GA1.2.386318973.1698073706',
        '_gat_UA-3524196-6': '1',
        '_ga': 'GA1.2.1776395458.1698073706',
        '_ga_ZSF3D6YSLC': 'GS1.1.1698073706.1.1.1698073757.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gid=GA1.2.386318973.1698073706; _gat_UA-3524196-6=1; _ga=GA1.2.1776395458.1698073706; _ga_ZSF3D6YSLC=GS1.1.1698073706.1.1.1698073757.0.0.0',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': {link},
        'locale': 'en',
        'tt': 'RFdvZ0Rm',
    }
 
    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{id}_1.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
    with open("captions.json", "r") as f:
        captions = json.load(f)
    captions.append(link)
    with open ("captions.json", "w") as f:
        json.dump(captions, f)
def checkDuplicate(urlsDownload):
    with open("captions.json", "r") as f:
        captions = json.load(f)
    new_urls = []
    for url in urlsDownload:
        for link in captions:
            if link == url:
                break
        else: 
            new_urls.append(url)
    return new_urls

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options)
driver.get("https://www.tiktok.com/")
#Change to Comedy tab
time.sleep(2)
comedy_btn = driver.find_element(By.XPATH, '//*[@id="main-content-explore_page"]/div/div[1]/div[1]/button[2]')
comedy_btn.click()
try:
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    videos = soup.find_all('div', {"class" : "tiktok-1as5cen-DivWrapper"})
    urlsToDownload = []
    for video in videos:
        urlsToDownload.append(video.a["href"])
    newUrlsToDownload = checkDuplicate(urlsToDownload)
    for index, url in enumerate(urlsToDownload):
        print(f"Downloading video: {index}")
        downloadVideo(url, index)
        time.sleep(10)
finally:
    driver.quit()

