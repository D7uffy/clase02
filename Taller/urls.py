# URLS DEL PROYECTO

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academia.urls')) 
    #path('', include('zoologicoApp.urls')) 

]



