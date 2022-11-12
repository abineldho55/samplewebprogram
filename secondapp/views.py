from django.shortcuts import render
from secondapp.forms import teacherforms

def home(request):
    if request.method=='POST':
        form=teacherforms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'secondapp/home.html',context={'form':teacherforms})

# Create your views here.
