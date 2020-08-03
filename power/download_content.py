#Basic Template

#Advanced Scraping



#Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Download Function BY XPATH
def downloadbyxpath(chromedriverpath, url, xpath):

	options = Options()
	options.headless = True
	options.add_argument("--headless")

	driver = webdriver.Chrome(chromedriverpath,options=options)
	driver.maximize_window()
	driver.get(url)

	ele = driver.find_elements_by_xpath(xpath+"/tbody/tr")
	keys = []
	values = []
	for val in ele:
		cur = val.text
		arr = cur.split(' ')
		key = ""
		for i in range(0,len(arr)-1):
			key = key + arr[i]
		value = arr[len(arr)-1]
		keys.append(key)
		values.append(value)

	ret = {0:keys, 1:values}
	return ret

#Calling Function (BY XPATH)
print(downloadbyxpath('./chromedriver', 'https://www.upsldc.org/real-time-data', '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/table'))

