from django.shortcuts import render, redirect

from .forms import Todoforms
from.models import CRUD
from.import views
# Create your views here.
def curd(request):
    if request.method=='POST':
       Vehicle_Number=request.POST.get('Vehicle_Number')
       Vehicle_type=request.POST.get('Vehicle_type')
       Vehicle_model=request.POST.get('Vehicle_type')
       Vehicle_description=request.POST.get('Vehicle_description')
       obj=CRUD(Vehicle_Number=Vehicle_Number,Vehicle_type=Vehicle_type,Vehicle_model=Vehicle_model,Vehicle_description=Vehicle_description)
       obj.save()

    return render(request,'curd.html')

def curdview(request):
    obj1=CRUD.objects.all()
    return render(request,'curdview.html',{'obj1':obj1})

def delete(request,crudid):
 crud=CRUD.objects.get(id=crudid)
 if request.method=='POST':
     crud.delete()
     return redirect('/')
 return render(request,'delete.html',{'crud':crud})

def update(request,id):
    crud=CRUD.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=crud)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'crud':crud,'form':form})
