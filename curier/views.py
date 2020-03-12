from django.shortcuts import render,redirect,HttpResponse
from .forms import CurierRegisterForm
from users.forms import UserRegisterForm
from .models import Curier,Changes
from django.core.mail import send_mail
from Lallog.models import Lalo,TestOrder
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
import datetime
import locale
def curier_register(request):
	if request.method=="POST":
		user_form = UserRegisterForm(data=request.POST)
		curier_form=CurierRegisterForm(data=request.POST,files=request.FILES)
		print(curier_form)
		if user_form.is_valid() and curier_form.is_valid():
			new_user= user_form.save()
			new_curier = Curier.objects.create(
				user=new_user,
				date_of_birth=curier_form.cleaned_data.get('date_of_birth'),
				photo=request.FILES['photo'],
				experience=curier_form.cleaned_data.get('experience'),
				phone=curier_form.cleaned_data.get('phone'),
				)
			new_curier.save()
			text=new_user.username+" "+str(curier_form.cleaned_data.get('date_of_birth'))+" "+str(curier_form.cleaned_data.get('phone'))
			send_mail("new curier",text,'tleugazy98@gmail.com',['jakesablee@gmail.com'],fail_silently=False)
			return redirect("Home")
		return HttpResponse("Error")

	else:
		form_user = UserRegisterForm()
		curier_user = CurierRegisterForm()
		cxt={
		   "register_form":form_user,
		   "curier_form":curier_user,
		}
		return render(request,"curiers/register.html",context=cxt)

def private_сurier(request):
	curier = request.user.mycurier
	today  = timezone.now()
	orders = TestOrder.objects.filter(status="Забрал")
	cxt={
	    'orders':orders,
	}
	return render(request,"curiers/private.html",context=cxt)

def private_сurier2(request):
	curier = request.user.mycurier
	today  = timezone.now()
	all_empty_orders = TestOrder.objects.all().filter(curier=None)
	cxt={
	    'empty_orders':all_empty_orders
	}
	return render(request,"curiers/Moi_zakazy.html",context=cxt)

def curier_select(request,id):
	current_test_order = TestOrder.objects.get(pk=id)
	# change = Changes.objects.create(user=request.user.mycurier,balance_before=request.user.mycurier.balance-((current_test_order.itog*35)//100),summa=((current_test_order.itog*35)//100),reason="Взял Заказ")
	# change.save()
	current_test_order.curier = request.user.mycurier
	current_test_order.save()
	return redirect("private_сurier")
	
def curier_cancel(request,id):
	current_test_order = TestOrder.objects.get(pk=id)

	# current_test_order.curier.balance+=((current_test_order.itog*35)//100)-50
	current_test_order.curier.balance-=50
	change = Changes.objects.create(user=request.user.mycurier,balance_before=current_test_order.curier.balance,summa=-50,reason="Отменил Заказ")
	change.save()
	current_test_order.curier.save()
	current_test_order.curier = None
	current_test_order.status = "Ожидание"
	current_test_order.save()

	return redirect("private_сurier")

def rashet_view(request,day):
	curier = request.user.mycurier
	orders_completed=None
	alldaysorders=curier.choiced_curier.all().filter(status="Доставлен")
	if day=="all":
	    orders_completed = curier.choiced_curier.all().filter(status="Доставлен")
	elif day=="today":
		locale.setlocale(locale.LC_ALL, "ru")
		mydate= datetime.date.today().strftime("%d %B")
		orders_completed = curier.choiced_curier.all().filter(status="Доставлен",to_date=mydate)
	elif day=="yesterday":
		locale.setlocale(locale.LC_ALL, "ru")
		mydate1=datetime.date.today() - datetime.timedelta(days=1)
		mydate1=mydate1.strftime("%d %B")
		print(mydate1)
		orders_completed = curier.choiced_curier.all().filter(status="Доставлен",to_date=mydate1)
	else:
	    orders_completed = curier.choiced_curier.all().filter(status="Доставлен",to_date=day)
	mydata = list(orders_completed.values_list("to_date"))
	mydata1 = list(alldaysorders.values_list("to_date"))
	alldays=[]
	for i in mydata1:
	    alldays.append(i[0])
	alldays = set(alldays)
	days=[]
	for i in mydata:
	    days.append(i[0])
	days=set(days)
	analyze=[]
	for i in days:
	    order = orders_completed.filter(to_date=i)
	    sumi=0
	    for j in order:
	        sumi+=j.raschet
	    temp={
	    "day":i,
	    "sum":int(sumi)
	    }
	    analyze.append(temp)
	print(analyze)
	mydate= datetime.datetime.now()
	mydate1=datetime.date.today() + datetime.timedelta(days=1)
	ctx={
		"orders_completed":orders_completed,
		"analyze":analyze,
		"alldays":alldays,
		"today":mydate,
		"tomorrow":mydate1,
	}
	return render(request,"curiers/raschet.html",context=ctx)
def curier_history(request):
    histories = Changes.objects.all().filter(user=request.user.mycurier)
    total=0
    for i in histories:
    		if i.reason!="Пополнение Админом":
    				total+=i.summa
    ctx={
    "history":histories,
    "total":total,
    }
    return render(request,"curiers/history.html",context=ctx)