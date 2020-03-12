from django.shortcuts import render,redirect,HttpResponse
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from Lallog.models import Lalo,TestOrder
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import login,logout,authenticate
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import locale
def register(request):
	
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			username=form.cleaned_data.get('username')
			messages.success(request,'Ваш аккаунт создан')
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return redirect("Home")
	else:
		form = UserRegisterForm()
	cxt={
	   "register_form":form
	}
	return render(request,"users/register.html",context=cxt)


def user_login(request):
	if request.method=='POST':
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			try:
				if user.curier.is_available:
					return redirect("private_сurier")
				else:
					return HttpResponse("вас не утвердили")
			except:
				return redirect("Home")
		else:
			messages.warning(request,"У нас нет такого пользователя")
			return redirect("user_login")
	else:	
		return render(request,"users/log_in.html",{})
@csrf_exempt
def private_data(request):
	orders = TestOrder.objects.filter(client=request.user).exclude(status="доставлен").exclude(status="Доставлен")
	data=[]
	for i in orders:
		obj={}
		obj["id"]=i.pk
		obj["Компания"]=i.client.username
		obj["Откуда"]=i.from_address
		obj["Номер отправителя"]=i.from_phone
		obj["Куда"]=i.to
		obj["Номер получателя"]=i.to_phone
		obj["Вес"]=i.ves
		obj["Дата доставки"]= i.to_date
		obj["Доставить до"]= i.to_date_until
		obj["Итог"] = i.itog
		obj["Наличные"] = i.nal
		obj["К выплате"] = i.raschet
		obj["Статус"] = i.status
		try:
			obj["Курьер"] = i.curier.user.username
			obj["Номер курьера"] = i.curier.phone
		except:
			obj["Курьер"] = "Ждем курьера"
			obj["Номер курьера"]="Ждем курьера"
		
		data.append(obj)
	cxt={
	    'orders':data,
	}
	return JsonResponse(cxt)
def remove_order(request,id):
	order=TestOrder.objects.get(pk=id)
	order.delete()
	return redirect("private")
def private(request):
	return render(request,"users/private.html")
	    
	    
	return render(request,"users/private.html",context=data)
def user_logout(request):
	logout(request)
	return redirect("Home")

def private_success(request,day):
	curier = TestOrder.objects.filter(client=request.user)
	orders_completed=None
	alldaysorders=curier.all().filter(status="Доставлен")
	if day=="all":
	    orders_completed = TestOrder.objects.filter(client=request.user,status="Доставлен")
	elif day=="today":
		locale.setlocale(locale.LC_ALL, "ru")
		mydate= datetime.date.today().strftime("%d %B")
		orders_completed = curier.all().filter(status="Доставлен",to_date=mydate)
	elif day=="yesterday":
		locale.setlocale(locale.LC_ALL, "ru")
		mydate1=datetime.date.today() - datetime.timedelta(days=1)
		mydate1=mydate1.strftime("%d %B")
		print(mydate1)
		orders_completed = curier.all().filter(status="Доставлен",to_date=mydate1)
	else:
	    orders_completed = curier.all().filter(status="Доставлен",to_date=day)
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

	mydate= datetime.datetime.now()
	mydate1=datetime.date.today() + datetime.timedelta(days=1)
	ctx={
		"orders_completed":orders_completed,
		"analyze":analyze,
		"alldays":alldays,
		"today":mydate,
		"tomorrow":mydate1,
	}
	return render(request,"users/private2.html",context=ctx)
def private_raschet(request):
    client = request.user
    orders_completed = TestOrder.objects.filter(status="Доставлен",client=client)
    mydata = list(orders_completed.values_list("to_date"))
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
    ctx={
		"analyze":analyze,
	}
    return render(request,"users/raschet.html",context=ctx)
def edit(request):
	if request.method=='POST':
		user_form= UserEditForm(instance=request.user, data=request.POST)
		profile_form=ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect("private")

	else:
		user_form = UserEditForm(instance=request.user)
		profile_form=ProfileEditForm(instance=request.user.profile)
		return render(request, 'users/edit.html', {'user_form':user_form, 'profile_form':profile_form})


