from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import EmployeeModel
from django.contrib import messages


# Create your views here.
def showindex(request):
    ef=EmployeeForm()
    return render(request,"index.html",{"form":ef})


def saveemployee(request):
    id=request.POST["f_idno"]
    nam=request.POST["f_name"]
    sal=request.POST["f_sal"]
    EmployeeModel(idno=id,name=nam,salary=sal).save()
    messages.success(request,"details saved succesfully")
    return redirect('main')