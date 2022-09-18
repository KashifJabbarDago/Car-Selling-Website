
from django.shortcuts import render,HttpResponse
from carblog.models import OwnSellCars,CustomersCarForSell
from django.contrib import messages
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your views here.
def blogHome(request):
    Customer_data = CustomersCarForSell.objects.all()
    data = OwnSellCars.objects.all()
    print(Customer_data)
    params = {'data':data,'customer_data':Customer_data}
    return render(request,'carblog/carbloghome.html',params)

def carSell(request):
    if request.method == 'POST' and request.FILES['carimage']:
        car_category = request.POST.get('category')
        car_name = request.POST.get('carname')
        car_model = request.POST.get('carmodel')
        car_color = request.POST.get('carcolor')
        owner_phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        car_price = request.POST.get('carprice')
        pub_date = request.POST.get('pubdate')
        car_image = request.FILES['carimage']
        fs = FileSystemStorage()
        filename = fs.save(car_image.name,car_image)
        upload_file = fs.url(filename)
        if len(car_name) <2 or len(owner_phone) <5 or len(car_model)< 3:
            messages.error(request,"Form not submitted!, Please fill the form correctly")
        else:
            customer_data = CustomersCarForSell(customer_car_category=car_category,customer_car_name=car_name,
            customer_number=owner_phone,customer_location=msg,customer_car_model=car_model,customer_car_color=car_color,
            customer_uploading_date=pub_date,customer_car_price=car_price,customer_car_image=car_image)
            customer_data.save()
            messages.success(request,"Form submitted successfully")
        
    return render(request,'carblog/sellcars.html')