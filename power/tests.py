def enable_download_in_headless_chrome(driver, download_dir):
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)

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


def getfile(path, minms, maxms):
	csv_file = pd.read_csv(path)
	ac = list(csv_file['Actual_flow'])
	# freq = csv_file['Frequency']
	date = list(csv_file['Date_updated'])
	outlier = []
	# for (i,row) in enumerate(ac):

	context = {
		'ac':ac,
		'date':date,
	}
	# ret = []
	# for i in range(0,csv_file.shape[0]):
	# 	ac_cur = ac[i]
	# 	# freq_cur = freq[i]
	# 	date_cur = date[i]

	# 	if ac_cur<minms['Actual_flow'] or ac_cur>maxms['Actual_flow']:
	# 		if ac_cur<minms['Actual_flow']:
	# 			res = {'Actual_flow' : ac_cur, 'Date_updated' : date_cur, 'Message' : 'Actual Flow is less than ATC'}
	# 		else:
	# 			res = {'Actual_flow' : ac_cur,  'Date_updated' : date_cur, 'Message' : 'Actual Flow is more than ATC'}
	# 		ret.append(res)
	# 	# elif freq_cur<minms['Frequency'] or freq_cur>maxms['Frequency']:
	# 	# 	if freq_cur<minms['Frequency']:
	# 	# 		res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : 'Less Frequency used'}
	# 	# 	else:
	# 	# 		res = {'Actual_flow' : ac_cur, 'Frequency' : freq_cur, 'Date_updated' : date_cur, 'Message' : '<More Frequency used'}
	# 	# 	ret.append(res)

	return context

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


