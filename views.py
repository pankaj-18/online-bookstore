from django.shortcuts import render,HttpResponseRedirect
from .forms import Sellerregistration,Customerregistraion,Deleteregistraion,Updateregistraion,Accessregistraion,Purchaseregistraion,Searchregistraion,Sbpregistraion
from .models import Seller,Customer,Delete,Update,Access,Search,Purchase,Sbp
# from django.contrib.auth.forms import UserCreationForm
# add
def add(request):
    if request.method =='POST':
        sell=Sellerregistration(request.POST)
        if sell.is_valid():
            sell.save()
    else:
        sell = Sellerregistration()
    return render(request,'add.html',{'form':sell})


# update
def update(request):
    up=Updateregistraion
    if request.method =='POST':
        up=Updateregistraion(request.POST)
        if up.is_valid():
            up.save()
    context={'form':up}
    return render(request,'update.html',context)


# delete
def delete(request):
    dl=Deleteregistraion
    if request.method =='POST':
        dl=Deleteregistraion(request.POST)
        if dl.is_valid():
            dl.save()
    context={'form':dl}
    return render(request,'delete.html',context)


def signup(request):
    sup=Customerregistraion
    if request.method =='POST':
        sup=Customerregistraion(request.POST)
        if sup.is_valid():
            sup.save()
    context={'form':sup}
    return render(request,'signup.html',context)

def purchase(request):
    pc=Purchaseregistraion
    if request.method =='POST':
        pc=Purchaseregistraion(request.POST)
        if pc.is_valid():
            pc.save()
    context={'form':pc}
    return render(request,'purchhase.html',context)

def search(request):
    sh=Searchregistraion
    if request.method =='POST':
        sh=Searchregistraion(request.POST)
        if sh.is_valid():
            sh.save()
    context={'form':sh}
    return render(request,'search.html',context)

def access(request):
    ac=Accessregistraion
    if request.method =='POST':
        ac=Accessregistraion(request.POST)
        if ac.is_valid():
            ac.save()
    context={'form':ac}
    return render(request,'accesslist.html',context)



def sbp(request):
    sb=Sbpregistraion
    if request.method =='POST':
        sb=Sbpregistraion(request.POST)
        if sb.is_valid():
            sb.save()
    context={'form':sb}
    return render(request,'sbp.html',context)