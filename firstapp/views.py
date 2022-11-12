from django.shortcuts import render
from firstapp.forms import studentforms

def student(request):
    if request.method=='POST':
        form=studentforms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'firstapp/student.html',context={'form':studentforms})


# Create your views here.
