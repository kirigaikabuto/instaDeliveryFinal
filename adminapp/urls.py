
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.index,name="curiers"),
    path("curiers/balance_add_form/<int:id>/",views.balance_add_form,name="balance_add_form"),
    path("curiers/balance_add_form_action/",views.balance_add_form_action,name="balance_add_form_action"),
    path("curiers/search_action/",views.index,name="curier_search_action"),
    path("orders/all/",views.orders_all,name="orders_all"),
    path("orders/today/",views.orders_today,name="orders_today"),
    path("orders/all/live_search/",views.live_search,name="live_search"),

]
