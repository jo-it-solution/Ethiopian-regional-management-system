from django.shortcuts import render,redirect
from .models import regionalInfo
from .forms import regionalInfoform
from django.contrib import messages

def home(request):
    all_region = regionalInfo.objects.all()
    context = {'all_region':all_region}
    return render(request,'home.html',context=context)

def create_region(request):
    if request.method=='POST':
        form = regionalInfoform(request.POST,request.FILES)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'create_region.html',context=context)

        
        
    else:
        form = regionalInfoform()
        context = {'form':form}
        return render(request,'create_region.html',context=context)



def detail_region(request,pk):
    region=regionalInfo.objects.get(id=pk)
    context = {'region':region}
    return render(request,'detail_region.html',context=context)


def update_region(request,pk):
    region=regionalInfo.objects.get(id=pk)
    form = regionalInfoform(instance=region)
    if request.method=='POST':
        form = regionalInfoform(request.POST,request.FILES,instance=region)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form':form}
            messages.success(request,'sorry in valid form solution')
            return render(request,'create_region.html',context=context)
    else:
       
        context = {'form':form}
        return render(request,'create_region.html',context=context)
    

def delete_region(request,pk):
    region=regionalInfo.objects.get(id=pk)
    if request.method=='POST':
        region.delete()
        messages.success(request,'the region successfuly deleted')
        return redirect('home') 
    else:
         context = {'region':region}
         return render(request,'delete_region.html',context=context)

from django.contrib.auth.forms import UserCreationForm
def user_register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'user_register.html',context=context)

        
        
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request,'user_register.html',context=context)
# Create your views here.