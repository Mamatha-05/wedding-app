from django.shortcuts import render,redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wedding,Vendor,select
def home(request):
    return render(request,'home.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r login through vendor")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def Register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        conformation_password =request.POST['cnfm_password']
        select_user=request.POST['select_user']
        if select_user=='admin':
            select_user=True
        else :
            select_user=False
        if password == conformation_password:
            user = User.objects.filter(username=username)  
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'registration.html')
def user_dash(request):
    return render(request,'dashboard.html',)
def add_wedding(request):
    if request.method=="POST":
        name=request.POST['name']
        date=request.POST['date']
        location=request.POST['location']
        data=Wedding.objects.create(user=request.user,name=name,date=date,location=location)
        data.save()
        return redirect('home')
    return render(request,'Wedding.html')
def vendor_details(request):
    if request.method=="POST":
        name=request.POST['name']
        service=request.POST['service']
        contact_info=request.POST['contact_info']
        data=Vendor.objects.create(user=request.user,name=name,service=service,contact_info=contact_info)
        data.save()
        return redirect('services')
    return render(request,'vendor.html')
def service_list(request):
    data=Vendor.objects.filter(user=request.user)
    return render(request,'services.html',{'data':data,})
def weddings_view(request):
    wedding=True
    data=Wedding.objects.filter(user=request.user)
    return render(request,'weddings.html',{'data':data,'weddings':wedding})
def wedding_vendor(request):
    add_vendor=True
    data=Wedding.objects.filter(user=request.user)
    return render(request,'weddings.html',{'data':data,'add_vendor':add_vendor})
def add_vendors(request,pk):
    data=Wedding.objects.get(id=pk)
    selected=select.objects.filter(wedding=data)
    vendors=Vendor.objects.all()
    if request.method=='POST':
        vendor_id=request.POST['vendor']
        vendor=Vendor.objects.get(id=vendor_id)
        Select=select.objects.create(user=request.user,wedding=data,vendor=vendor)
        Select.save()
        return redirect('wedding_vendor')
    return render(request,'addvendors.html',{'data':data,'vendors':vendors,'selected':selected})
def delete_vendor(request,pk):
    data=select.objects.get(id=pk)
    data.delete()
    return redirect('wedding_vendor')
def wedding_vendor_list(request):
    checkvendors=True
    data=Wedding.objects.filter(user=request.user)
    return render(request,'weddings.html',{'checkvendors':checkvendors,'data':data})
def wedding_vendors_check(request,pk):
    data=Wedding.objects.get(id=pk)
    selected=select.objects.filter(wedding=data)
    return render(request,'vendor_wedding_list.html',{'selected':selected})
def my_vendor_list(request):
    pending=True
    vendors=Vendor.objects.filter(user=request.user)
    return render(request,'services.html',{'vendors':vendors,'pending':pending})
def vendor_wedding_requests(request,pk):
    checking=True
    vendor=Vendor.objects.get(id=pk,user=request.user)
    list=select.objects.filter(vendor=vendor,status="pending")
    return render(request,'vendor_pending_list.html',{'pendings':list,'checking':checking})
def vendor_confirmation(request,pk):
    data=select.objects.get(id=pk)
    if data.vendor.user == request.user:
        data.status = 'confirm'
        data.save()
    return redirect('my_vendor_list')
def check_confirmed(request):
    vendors=Vendor.objects.filter(user=request.user)
    return render(request,'services.html',{'vendors':vendors})
def confirmed_data(request,pk):
    vendor=Vendor.objects.get(id=pk,user=request.user)
    list=select.objects.filter(vendor=vendor,status="confirm")
    return render(request,'vendor_pending_list.html',{'pendings':list})
