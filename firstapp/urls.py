from django.urls import path
from firstapp import views
from django.contrib import admin

app_name="firstapp"

urlpatterns=[
    path("student/",views.student,name="first appname"),
    path('admin/', admin.site.urls),
]
