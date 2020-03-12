from django.urls import path
from . import views
# app_name="users"
urlpatterns = [
    path('register/', views.register,name="user_register"),
    path('user_login/',views.user_login,name ='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('private/data/',views.private_data,name="private_data"),
    path('private/',views.private,name="private"),
    path("private/success/<str:day>",views.private_success,name="private_success"),
    path("private/raschet/",views.private_raschet,name="private_raschet"),
    path('private/remove_order/<int:id>/',views.remove_order,name="remove_order"),
    path ('edit/',views.edit, name= 'edit'),


]
