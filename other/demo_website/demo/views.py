from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse

from .models import Sector, Electricity
# Create your views here.
import json

#Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def index(request):
	if request.method=='POST':
		e = Electricity()
		e.Actual_flow_min = request.POST['Actual_flow_min']
		e.Actual_flow_max = request.POST['Actual_flow_max']
		e.Frequency_min = request.POST['Frequency_min']
		e.Frequency_max = request.POST['Frequency_max']
		e.save()
		request.session['message']="Data submitted"
		return redirect('/demo/')
	else :
		context = {}
		if 'message' in request.session.keys():
			context['message'] = request.session['message']
			del request.session['message']

		return render(request,'demo/index.html', context)

#Basic Template

#Advanced Scraping






# For Headless=True
def enable_download_in_headless_chrome(driver, download_dir):
    # add missing support for chrome "send_command"  to selenium webdriver
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    command_result = driver.execute("send_command", params)



# Download PDF Function
def downloadpdf(chromedriverpath, url):

	options = Options()
	#options.headless = True
	options.add_argument("--headless")

	driver = webdriver.Chrome(chromedriverpath,options=options)

	enable_download_in_headless_chrome(driver, "download")

	driver.maximize_window()

	driver.get(url)

	aTagsInLi = driver.find_elements_by_css_selector('li a')
	for a in aTagsInLi:
		val = a.get_attribute('href')
		arr = val.split('.')
		length = len(arr)
		ext = arr[length-1]
		print(ext)
		if ext == 'csv':
			a.click()
	time.sleep(2)
	driver.close()


# Calling Function
downloadpdf('/usr/bin/chromedriver', 'https://secure-video-calling.herokuapp.com/')



# def get_rows(request):
# 	name = request.POST['name']
# 	s = get_object_or_404(Sector,name=name)
# 	data = json.loads(s.fields)
# 	return HttpResponse("hello")
# 	# return JsonResponse(data, safe=False)

# name = request.POST['name']
# 		s = Sector(name=name)
# 		temp_dict = json.loads(s.fields)
# 		for field in temp_dict.keys():
# 			temp_dict[field] = request.POST[field]
# 		s.fields = json.dumps(temp_dict)
# 		s.save()