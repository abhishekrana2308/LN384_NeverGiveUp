from django.shortcuts import render,redirect, get_object_or_404

from django.http import HttpResponse,JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from .models import Person,Sector,Board, Notification, Table, Alert


import time
import pandas as pd
from django.core.mail import send_mail
import json


################# CURRENT ###################

def save_table(request):
	t = Table()
	if Table.objects.filter(name=request.POST['name'],uid=request.session['uid']).exists() == False:
		t.name = request.POST['name']
		t.url = request.POST['url']
		t.xpath = request.POST['xpath']
		t.uid = request.session['uid']
		t.save()
		request.session['table_name'] = t.name
	return redirect('/power/analysis')

def analysis(request):
	# downloadpdftest('./chromedriver', 'https://secure-video-calling.herokuapp.com/' )
	# downloadpdf('./chromedriver', 'https://npp.gov.in/publishedReports')
	# minms = {'Actual_flow':6020, 'Frequency':55}
	# maxms = {'Actual_flow':6200, 'Frequency':65}
	# x = getfile("./download/Notice 2020 - Sheet1.csv", minms, maxms)
	# print(x)
	if request.GET.get('tablename'):
		request.session['table_name'] = request.GET.get('tablename')
	context = {}
	if 'uid' in request.session:
		uid = request.session['uid']
	else:
		return HttpResponse("Please Login")
	if 'table_name' in request.session:
		context['table_name'] = request.session['table_name']
		context['data'] = Table.objects.get(uid=uid,name=request.session['table_name'])
	
	return render(request, 'power/analysis.html', context)

# def get_data(request):
# 	# table_name = request.POST['table_name']
# 	# t = get_object_or_404(Table, name = table_name)
# 	# url = t.url
# 	url = 'https://www.upsldc.org/real-time-data'
# 	# xpath = t.xpath
# 	xpath = '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/table'
# 	data = downloadbyxpath('./chromedriver', url, xpath)
	
# 	return JsonResponse(data, safe=False)

# url = 'https://www.delhisldc.org/'
# 	# 
# 	xpath = '/html/body/form/div[3]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td/table'
def get_data(request):
	table_name = request.POST['table_name']
	t = get_object_or_404(Table, name = table_name, uid=request.session['uid'])
	url = t.url
	xpath = t.xpath
	
	data = downloadbyxpath('/usr/bin/chromedriver', url, xpath)

	return JsonResponse(data, safe=False)


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

def history(request):
	if 'uid' in request.session:
		uid = request.session['uid']
		results = Table.objects.filter(uid=uid)
		return render(request, 'power/history.html', context={"results":results})
	else:
		return HttpResponse("Please Login")


def alert(request):
	if 'uid' in request.session:
		uid = request.session['uid']
		results = Alert.objects.filter(uid=uid)
		return render(request, 'power/alerts.html', context={"results":results})
	else:
		return HttpResponse("Please Login")


def getalert(request):
	alertid = request.GET.get('alertid')
	print(alertid)
	alert = Alert.objects.get(pk=alertid)
	print(alert)
	return render(request, 'power/get_alert.html', context={"alert":alert})


def sendmailall(request):
	uid = request.session['uid']
	user_det = Person(pk=uid)
	data = Alert.objects.filter(uid=uid)
	ret = {}
	ret_html = {}
	i=0
	for val in data:
		res = {'Table Name' : val.name, 'Type' : val.key, 'Avy Value' : val.avgvalue, 'Start Time' : val.starttime, 'End Time' : val.endtime}
		ret[i] = res
		html = "       " 
		html += "           Table Name :  "+val.name
		html += "          Type : "+val.key
		html += "          Avg Value : "+val.avgvalue

		html += "          Start Time : "+val.starttime
		html += "          End Time : "+val.endtime

		html += "                  " 
		ret_html[i] = html
		i = i+1
	ret = json.dumps(ret)
	ret_html = json.dumps(ret_html)
	print(ret_html)

	send_mail(
		'Alerts to Power Sector of India',
		ret_html,
		'rishikeshsahu14101998@gmail.com',
		['rishikeshsahu2017@gmail.com'],
		fail_silently=False,
	)
	return HttpResponse("SuccesFully Mailed to your Account")


def addalert(request):
	name = request.POST.get('name')
	freq = request.POST.get('freq')
	starttime = request.POST.get('starttime')
	endtime = request.POST.get('endtime')
	minmfreq = request.POST.get('minmfreq')
	maxmfreq = request.POST.get('maxmfreq')
	print(name)
	print(freq)
	print(starttime)
	print(minmfreq)

	user_det = Person(pk=request.session['uid'])

	a = Alert()
	a.uid = request.session['uid']
	a.name = name
	a.key = "Frequency"
	a.avgvalue = freq
	a.starttime = starttime
	a.endtime = endtime
	a.minmattr = "Minm Frequency"
	a.minmvalue = minmfreq
	a.maxmattr = "Maxm Frequency"
	a.maxmvalue = maxmfreq
	a.save()


	html = "       " 
	html += "           Table Name :  "+name
	html += "          Type : Frequency"
	html += "          Avg Value : "+freq
	html += "          Start Time : "+starttime
	html += "          End Time : "+endtime
	html += "                  " 

	send_mail(
		'Alerts to Power Sector of India',
		html,
		'rishikeshsahu14101998@gmail.com',
		['rishikeshsahu2017@gmail.com'],
		fail_silently=False,
	)



	return HttpResponse("Success")
# def savedcharts(request):
# 	if 'uid' in request.session:
# 		uid = request.session['uid']
# 		results = Chart.objects.filter(uid=uid)
# 		return render(request, 'power/savedcharts.html', context={"results":results})
# 	else:
# 		return HttpResponse("Please Login")

###################### //// CURRENT #################


def index(request):
	message = ""
	message_type = ""
	if 'message' in request.session:
		message = request.session['message']
	
	if 'type' in request.session:
		message_type = request.session['type']
		
	request.session['message']=""

	return render(request,'power/index.html', context = {"message": message, "type" : message_type, "homelink":1})

def user_login(request):

	print(request.POST)
	email = request.POST['email']
	password = request.POST['password']
	print("inside user login====================")

	if Person.objects.filter(email=email, password=password, is_user=True).exists():
		p = Person.objects.get(email=email)
		request.session['uid']=p.id
		request.session['name']=p.name
		request.session['is_user']=p.is_user
		request.session['message']="Successfully Logged in";
		request.session['type'] = 1
		return redirect('/power/user_dash/')
	else:
		print("wrong email or password===============")
		request.session['message']="Wrong Email or Password";
		request.session['type'] = ""
		return redirect('/power/')



def user_signup(request):
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['password']

	if Person.objects.filter(email=email).exists():
		request.session['message']="Email Already Exists";
		request.session['type'] = ""
		return redirect('/power/')
	else:
		p = Person(name = name, email=email, password=password)
		p.save()
		request.session['uid']=p.id
		request.session['is_user']=p.is_user
		request.session['name']=p.name
		request.session['message']="Successfully Logged in";
		request.session['type'] = 1

		return redirect('/power/user_dash') 


def govt_login(request):
	email = request.POST['email']
	password = request.POST['password']

	if Person.objects.filter(email=email, password=password, is_user=False).exists():
		p = Person.objects.get(email=email)
		request.session['name']=p.name
		request.session['is_user']=p.is_user
		request.session['uid']=p.id
		request.session['message']="Successfully Logged in";
		request.session['type'] = 1
		return redirect('/power/govt_dash')
	else:
		request.session['message']="Wrong Email or Password";
		request.session['type'] = ""
		return redirect('/power/')


def govt_signup(request):
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['password']
	print("======inside govt signup=========")
	if Person.objects.filter(email=email).exists():
		print("=====email exists=======")
		request.session['message']="Email Already Exists";
		request.session['type'] = ""
		return redirect('/power/')
	else:
		p = Person(name = name, email=email, password=password, is_user=False)
		p.save()
		request.session['name']=p.name
		request.session['is_user']=p.is_user
		request.session['uid']=p.id
		print("=====logged in success=======")
		request.session['message']="Successfully Logged in";
		request.session['type'] = 1
		return redirect('/power/govt_dash') 



def logout(request):
	if 'uid' in request.session:
		del request.session['uid']
		del request.session['name']
		del request.session['is_user']
	request.session['message']="Successfully Logged out";
	request.session['type'] = 1
	return redirect('/power/')



def govt_dash(request):

	if 'uid' not in request.session:
		request.session['message']="Please login first"
		request.session['type']=""  # dont know the type

		redirect('/power/')

	uid = request.session['uid']
	
	p = Person.objects.get(pk=uid)
	all_boards = p.board_set.all()
	all_sectors = Sector.objects.all()
	all_states = Board.objects.values_list('state',flat=True).distinct().order_by('state')
	# all_boards = all_boards.value_list('sector', flat=True).order_by('sector')
	# print(type(all_states[0]))
	state = "all"
	sector = "555"

	# what if it comes through GET?
	if request.method == "POST":
		state = request.POST['state']
		sector = request.POST['sector']	

		if Sector.objects.filter(pk=sector).exists():
			# selected_sector = Sector.objects.get(pk=sector)
			all_boards = all_boards.filter(sector=sector)

			if state!="all":
				all_boards = all_boards.filter(state=state)
			# print("1")
		elif state!="all":
			all_boards = Board.objects.filter(state=state)
			# print(2)
	if 'message' in request.session:
		message = request.session['message']
		message_type = request.session['type']
	else:
		message = ""
		message_type = ""
	request.session['message']=""


	context = {
		"all_boards":all_boards,
		"all_sectors":all_sectors,
		"all_states":all_states,
		"message" : message,
		"type": message_type,
		"homelink" : 1,
		"state": state,
		"sector":sector
	}
	return render(request, "power/govt_dash.html", context);



def edit_profile(request):
	if 'uid' not in request.session:
		request.session['message']="Please login first"
		request.session['type']=""  # dont know the type

		redirect('/power/')

	if request.method=="POST":
		uid = request.session['uid']
		p = Person.objects.get(pk=uid)
		
		p.name = request.POST['name']
		p.email = request.POST['email']
		p.mob = request.POST['mobileno']
		p.aadhar = request.POST['aadhar']
		print(p.aadhar)
		p.save()
		request.session['message'] = "Successfully Updated Your Profile"
		request.session['type'] = 1
		request.session['name'] = p.name
		if p.is_user:
			return redirect('/power/edit_profile')
		else:
			return redirect('/power/edit_profile')

	else :
		uid = request.session['uid']
		p = Person.objects.get(pk=uid)
		if 'message' in request.session:
			message = request.session['message']
			message_type = request.session['type']
		else:
			message = ""
			message_type = ""

		request.session['message']=""
		context = {
			"name" : p.name,
			"email" : p.email,
			"mob" : p.mob,
			"aadhar" : p.aadhar,
			"message" : message,
			"type" :message_type
		}
		return render(request,'power/edit_profile.html', context)
    
def change_password(request):
	if 'uid' not in request.session:
		request.session['message']="Please login first"
		request.session['type']=""  # dont know the type

		redirect('/power/')


	uid = request.session['uid']
	p = Person.objects.get(pk=uid)

	p1 = request.POST['newpass']
	p2 = request.POST['reenterpass']

	# request.session['message']="Both passwords do not match"
	request.session['message'] = "Passwords do not match"
	request.session['type'] = ""
	if(p1==p2):
		p.password=p1
		p.save()
		request.session['message'] = "Successfully Updated Your Password"
		request.session['type'] = 1
		# request.session['message']="Password changed successfully"

	return redirect('/power/edit_profile')


def add_board(request):
	if 'uid' not in request.session:
		request.session['message']="Please login first"
		request.session['type']=""  # dont know the type

		redirect('/power/')


	uid = request.session['uid']
	person = Person.objects.get(pk=uid)

	sector_name = request.POST['sector']		
	state = request.POST['state']
	name = request.POST['name']
	url = request.POST['url']
	xpath = request.POST['xpath']

	sector = Sector.objects.get(pk=sector_name)


	b = Board(sector=sector,state=state, name = name ,person=person,url=url,xpath=xpath)
	b.save()
	request.session['message'] = "Data Added Successfully"
	request.session['type'] = 1

	return redirect('/power/govt_dash')



def user_dash(request):
	if 'uid' not in request.session:
		request.session['message']="Please login first"
		request.session['type']=""  # dont know the type

		redirect('/power/')

	all_boards = Board.objects.all()
	all_sectors = Sector.objects.all()
	all_states = Board.objects.values_list('state',flat=True).distinct().order_by('state')
	# all_boards = all_boards.value_list('sector', flat=True).order_by('sector')
	# print(type(all_states[0]))
	state="all"
	sector = "555"
	if request.method == "POST":
		state = request.POST['state']
		sector = request.POST['sector']	

		if Sector.objects.filter(pk=sector).exists():
			selected_sector = Sector.objects.get(pk=sector)
			all_boards = selected_sector.board_set.all()
			if state!="all":
				all_boards = all_boards.filter(state=state)
			# print("1")
		elif state!="all":
			all_boards = Board.objects.filter(state=state)
			# print(2)
	if 'message' in request.session:
		message = request.session['message']
		message_type = request.session['type']
	else:
		message = ""
		message_type = ""

	request.session['message']=""

	context = {
		"all_boards":all_boards,
		"all_sectors":all_sectors,
		"all_states":all_states,
		"message" : message,
		"type" : message_type,
		"homelink":1,
		"state":state,
		"sector":sector

	}

	return render(request, "power/user_dash.html", context);


def search(request):
	search = request.POST['search']
	state = request.POST['state']
	sector = request.POST['sector']
	print(state)
	print(sector)
	
	p = get_object_or_404(Person,pk=request.session['uid'])
	if(p.is_user):
		all_boards = Board.objects.all()
	else :
		all_boards = p.board_set.all()
	if state == "all" and sector == "555":
		data = list(all_boards.filter(name__contains=search).values())
	elif state == "all":
		data = list(all_boards.filter(name__contains=search,sector=sector).values())
	elif sector == "555":
		data = list(all_boards.filter(name__contains=search,state=state).values())
	else:
		data = list(all_boards.filter(name__contains=search,state=state,sector=sector).values())

	for row in data:
		sector_name = Sector.objects.get(pk=row['sector_id']).name
		row['sector']=sector_name
	# return HttpResponse("hi")
	return JsonResponse(data, safe=False)
	

def enable_notifications(request):
	board_id = request.POST['board_id']
	uid = request.session['uid']
	
	if(Notification.objects.filter(uid=uid, bid=board_id).exists()):
		n = Notification.objects.get(uid=uid, bid=board_id).delete()
		return HttpResponse("Notification Disabled")
	else:
		n = Notification(uid=uid, bid=board_id)	
		n.save()
	return HttpResponse("successfully enabled")



# # Scraping

def scraping(request,id):
	board = Board.objects.get(pk=id)
	url = board.url
	xpath = board.xpath
	print(url)
	print(xpath)
	options = Options()
	options.headless = True
	driver = webdriver.Chrome('./chromedriver', options=options)


	driver.get(url)
	driver.execute_script("console.error(document.lastModified)")
	log = driver.get_log('browser')
	for val in log:
	    if val['source'] == "console-api":
	        message = val['message']
	        message = message.split('"')
	        message = message[1]
	        
	b = get_object_or_404(Board, pk=id)
	uid = request.session['uid']
	enable=""
	if(Notification.objects.filter(uid=uid, bid=id).exists()):
		enable=1
	return render(request, 'power/scrap_data.html', context = {"message" : message, "board" : b,"enable":enable})

def scrap_data(request):
    url = request.POST.get('url')
    xpath = request.POST.get('xpath')
    print(url)
    print(xpath)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('./chromedriver', options=options)


    driver.get(url)

    data = driver.find_elements_by_xpath(xpath)

    html=""
    for val in data:
        html += val.get_attribute("outerHTML")
    driver.close()

    #My HTML
    my_html = ""

    return HttpResponse(html+my_html)



