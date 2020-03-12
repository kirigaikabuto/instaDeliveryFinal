from django.shortcuts import render,redirect
from django.http import JsonResponse
from curier.models import Curier,Changes
from Lallog.models import TestOrder
from django.utils import timezone
import datetime
import locale
from dal import autocomplete
from django.views.decorators.csrf import csrf_exempt
import json
def index(request):
    curiers=None
    if request.method=="POST":
        username = request.POST.get("search")
        curiers = Curier.objects.filter(user__username__contains=username)
    else:
        curiers = Curier.objects.all()
    cxt={
        "curiers":curiers

    }
    return render(request,"adminapp/curiers.html",context=cxt)
def balance_add_form(request,id):
    current_curier = Curier.objects.get(pk=id)
    ctx={
        "curier":current_curier
    }
    return render(request,"adminapp/curiers_balance_form.html",context=ctx)
def balance_add_form_action(request):
    id=int(request.POST.get("id"))
    balance=int(request.POST.get("balance"))
    print(id,balance)
    curren_curier = Curier.objects.get(pk=id)
    curren_curier.balance=curren_curier.balance+balance
    change = Changes.objects.create(user=curren_curier,balance_before=curren_curier.balance,summa=balance,reason="Пополнение Админом")
    change.save()
    curren_curier.save()
    return redirect("curiers")
def orders_all(request):
    orders = None
    locale.setlocale(locale.LC_ALL, "ru")
    if request.method == "POST":
        value = request.POST.get("search")
        field = request.POST.get("parameter")
        if field == "curier":
            orders = TestOrder.objects.filter(curier__user__username__contains=value)
        elif field == "client":
            orders = TestOrder.objects.filter(client__username__contains=value)
        elif field == "to_date":
            orders = TestOrder.objects.filter(to_date__contains=value)
    else:
        orders = TestOrder.objects.all()
    fields = [field.name for field in TestOrder._meta.get_fields()]

    ctx = {
        "orders": orders,
        "fields": fields
    }
    return render(request, "adminapp/orders.html", context=ctx)
def orders_today(request):
    orders=None
    locale.setlocale(locale.LC_ALL, "ru")
    if request.method=="POST":
        value = request.POST.get("search")
        field = request.POST.get("parameter")
        if field=="curier":
            orders=TestOrder.objects.filter(curier__user__username__contains=value)
        elif field=="client":
            orders=TestOrder.objects.filter(client__username__contains=value)
        elif field=="to_date":
            orders=TestOrder.objects.filter(to_date__contains=value)
    else:
        mydate= datetime.date.today().strftime("%d %B")
        print(mydate)
        orders = TestOrder.objects.filter(to_date=mydate)
    fields=[field.name for field in TestOrder._meta.get_fields()]

    ctx={
        "orders":orders,
        "fields":fields
    }
    return render(request,"adminapp/orders.html",context=ctx)
@csrf_exempt
def live_search(request):
    mydata = json.loads(request.read().decode('utf-8'))
    parameter = mydata.get("parameter")
    search = mydata.get("search")
    orders=[]
    if parameter=="curier":
        testorders=TestOrder.objects.filter(curier__user__username__contains=search)
        curiers = [x.curier.user.username for x in testorders]
        for i in curiers:
            if i not in orders:
                orders.append(i)
    elif parameter=="client":
        testorders = TestOrder.objects.filter(client__username__contains=search)
        clients = [x.client.username for x in testorders]
        for i in clients:
            if i not in orders:
                orders.append(i)
    elif parameter=="to_date":
        testorders = TestOrder.objects.filter(to_date__contains=search)
        dates = [x.to_date for x in testorders]

        for i in dates:
            if i not in orders:
                orders.append(i)
    otvet = {
        "message": "Заявка отправлена!",
        "arr": json.dumps(orders)
    }
    return JsonResponse(otvet)

