from django.urls import path
from mainapp import views
from django.contrib import admin

app_name="mainapp"

urlpatterns=[
    path("index/",views.index,name="main appname"),
    path('admin/', admin.site.urls),
]