from django.urls import path
from . import views 
from Map.views import post_order
urlpatterns = [
path('',views.index,name="Home"),
path('post/<int:id>/',views.post_detail, name="post_detail"),
path('post/new/',views.post_new, name="post_new"),
path('maps/kalkul',views.kalkul, name="kalkul"),
path("maps/kalkul/send/",views.get_calcul,name="get_calcul"),
path("curiers/private_сurier/status/change/",views.status_change,name="status_change"),
path("curiers/private_сurier/ajax/example/",views.all_curier_data,name="all_curier_data"),
path("curiers/private_сurier/order/cancel/",views.order_cancel,name="order_cancel"),
path('maps/post/order/',post_order, name ='post_order'),
]