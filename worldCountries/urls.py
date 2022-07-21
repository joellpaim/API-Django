from django.contrib import admin
from django.urls import path
#from django.conf.urls import url, include
from django.urls.conf import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^', include('countries.urls')),
]
