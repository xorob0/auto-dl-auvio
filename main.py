#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import re
import os
import time

showName = re.split('\?', re.split('_', sys.argv[1])[1])[0]

while True:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1366x768")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(sys.argv[1])

    mediaCards = driver.find_elements_by_class_name("rtbf-media-item")

    existingFiles = os.listdir(sys.argv[2])

    for mediaCard in mediaCards:
        href = mediaCard.find_element_by_class_name('www-faux-link').get_attribute("href")
        if re.match('https://www.rtbf.be/auvio/detail_'+showName+'-S?.*', href) is not None:
            episode = re.split('\s', mediaCard.find_element_by_tag_name('h4').text)[1]
            season = re.split('\s', mediaCard.find_element_by_tag_name('h3').text)[-1]
            id = re.split('=', re.split('\?', href)[-1])[-1]
            name = showName + '-' + season + 'E' + str(episode) + '-' + str(id) +'.mp4'

            if not name in existingFiles:
                os.system("youtube-dl " + href + ' -o ' + sys.argv[2] +'/'+ name )

    driver.quit()

    time.sleep(sys.argv[3])