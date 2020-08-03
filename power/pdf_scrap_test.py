#Basic Template

#Advanced Scraping



#Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# For Headless=True
def enable_download_in_headless_chrome(driver, download_dir):
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)



# Download PDF Function
def downloadpdftest(chromedriverpath, url):

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	chrome_options.headless = True
	#options.add_argument("--headless")
	#options.add_argument('--no-sandbox')

	driver = webdriver.Chrome(chromedriverpath,chrome_options=chrome_options)

	enable_download_in_headless_chrome(driver, "./download")

	driver.maximize_window()
	a_url=""
	driver.get(url)

	aTagsInLi = driver.find_elements_by_css_selector('a')
	for a in aTagsInLi:
		print(a)
		val = a.get_attribute('href')
		arr = val.split('.')
		length = len(arr)
		ext = arr[length-1]
		if ext == 'csv':
			a.click()
			time.sleep(2)



# Calling Function
downloadpdftest('/usr/bin/chromedriver', 'https://secure-video-calling.herokuapp.com/')
