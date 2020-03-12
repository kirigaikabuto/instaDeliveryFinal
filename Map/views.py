from django.shortcuts import render, HttpResponse
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
	return render(request, "maps/index.html")
@csrf_exempt
def post_order(request):
		mydate= datetime.datetime.now()
		mydate1=datetime.date.today() + datetime.timedelta(days=1)
		mydate2=datetime.date.today() + datetime.timedelta(days=2)
		mydate3=datetime.date.today() + datetime.timedelta(days=3)
		mydate4=datetime.date.today() + datetime.timedelta(days=4)
		mydate5=datetime.date.today() + datetime.timedelta(days=5)
		mydata = json.loads(request.body)
		print(mydata)
		context={
		'mydate': mydate, 'mydate1': mydate1,'mydate2': mydate2, 'mydate3': mydate3,'mydate4': mydate4,'mydate5': mydate5,
		'from':mydata["orig"],
		'to':mydata["dest"],
		'distance':mydata["kilometr"]

		}
		data={
		"message":"asdsd"
		}
		return JsonResponse(data)
		# otvet = {
		# "message":"all good"
		# }
		# return JsonResponse(otvet)
