from django.shortcuts import render,redirect, get_object_or_404

from django.http import HttpResponse,JsonResponse

from .models import Sector,Board

def index(request):
    # request.session['message']=""
    # # haha_hello

    # message = ""
    # message_type = ""
    # if 'message' in request.session:
    #     message = request.session['message']

    # if 'type' in request.session:
    #     message_type = request.session['type']
        
    # request.session['message']=""
    # # haha_hello
    return render(request,'power/index.html') # , context = {"message": message, "type" : message_type, "homelink":1}


def user_dash(request):
	# if 'uid' not in request.session:
	# 	request.session['message']="Please login first"
	# 	request.session['type']=""  # dont know the type

	# 	redirect('/power/')

	all_boards = Board.objects.all()
	all_sectors = Sector.objects.all()
	all_states = Board.objects.values_list('state',flat=True).distinct().order_by('state')

	# state="all"
	# sector = "555"
	# if request.method == "POST":
	# 	state = request.POST['state']
	# 	sector = request.POST['sector']	

	# 	if Sector.objects.filter(pk=sector).exists():
	# 		selected_sector = Sector.objects.get(pk=sector)
	# 		all_boards = selected_sector.board_set.all()
	# 		if state!="all":
	# 			all_boards = all_boards.filter(state=state)
	# 		# print("1")
	# 	elif state!="all":
	# 		all_boards = Board.objects.filter(state=state)
	# 		# print(2)
	# if 'message' in request.session:
	# 	message = request.session['message']
	# 	message_type = request.session['type']
	# else:
	# 	message = ""
	# 	message_type = ""

	# request.session['message']=""

	context = {
		"all_boards":all_boards,
		"all_sectors":all_sectors,
		"all_states":all_states,
		# "message" : message,
		# "type" : message_type,
		# "homelink":1,
		# "state":state,
		# "sector":sector

	}

	return render(request, "power/user_dash.html", context)