from django.urls import path
from secondapp import views
from django.contrib import admin

app_name="secondapp"

urlpatterns=[
    path("home/",views.home,name="second appname"),
    path('admin/', admin.site.urls),
]