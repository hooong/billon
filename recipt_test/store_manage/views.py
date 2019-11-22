from django.shortcuts import render, redirect
from .models import *
from .forms import *

def viewStore(request):
    if request.user.is_authenticated:
        recipts = Recipt.objects.filter(user=request.user)

        context = {'recipts':recipts}
    else:
        context = {}
    return render(request, 'viewStores.html',context)

def registrecipt(request):
    if request.method=='POST':
        reciptform = Recipt_Form(request.POST)
        if reciptform.is_valid():
            recipt = reciptform.save(commit=False)
            recipt.user = request.user    
            recipt.save()

        return redirect('viewstore')

    else:
        form = Recipt_Form()
        
        context = {'form':form}
        return render(request,'registrecipt.html',context)