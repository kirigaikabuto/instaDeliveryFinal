
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Lallog.urls')),
    path('users/',include('users.urls')),
    path('curiers/',include('curier.urls')),
    path('maps/', include('Map.urls')),
    path("adminpanel/",include("adminapp.urls"))
    
  
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)