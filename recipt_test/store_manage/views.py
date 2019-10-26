from django.shortcuts import render, redirect
from .models import *
from .forms import *

def viewStore(request):
    stores = Store.objects.filter(clerk=request.user)

    context = {'stores':stores}
    return render(request, 'viewStores.html',context)

def regitsStore(request):
    if request.method=='POST':
        storeform = Store_Form(request.POST)
        if storeform.is_valid():
            store = storeform.save(commit=False)
            store.clerk = request.user    
            store.save()

        return redirect('viewstore')

    else:
        form = Store_Form()
        
        context = {'form':form}
        return render(request,'registStore.html',context)