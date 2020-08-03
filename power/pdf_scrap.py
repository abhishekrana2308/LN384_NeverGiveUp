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
def downloadpdf(chromedriverpath, url):

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--no-sandbox')
	#options.headless = True
	#options.add_argument("--headless")
	#options.add_argument('--no-sandbox')

	driver = webdriver.Chrome(chromedriverpath,chrome_options=chrome_options)

	enable_download_in_headless_chrome(driver, "./download")

	driver.maximize_window()
	a_url=""
	driver.get(url)

	ele = driver.find_elements_by_xpath("//*[contains(text(), 'Daily Generation Reports')]")
	print(ele)
	for val in ele:
		val.click()
		aTagsInLi = driver.find_elements_by_css_selector('a')
		for a in aTagsInLi:
			val = a.get_attribute('href')
			print(val)
			arr = val.split('.')
			length = len(arr)
			ext = arr[length-1]
			name = arr[length-2]
			print(ext)
			if ext == 'xls' and "dgr" in name:
				print("_______I want this")
				a.click()
				time.sleep(5)


# Calling Function
downloadpdf('./chromedriver', 'https://npp.gov.in/publishedReports')
