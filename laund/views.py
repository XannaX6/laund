from django.shortcuts import render, redirect

# Create your views here.
from .models import Service,Product,Booking,Order
import uuid

def home(request):
 services = Service.objects.all().order_by('price')[:6] # show top services
 context = {
'services': services
 }
 return render(request, 'laund/home.html', context)
#  return render(request, 'laund/home.html', {'services': Service.objects.all()})

def shop(request):
 return render(request,'laund/shop.html',{'products':Product.objects.all()})

def booking(request):
 if request.method == 'POST':
  Booking.objects.create(
   name=request.POST['name'],
   phone=request.POST['phone'],
   address=request.POST['address'],
   service=request.POST['service'],
   pickup_date=request.POST['date'],
   pickup_time=request.POST['time']
  )
  return redirect('pay')
 return render(request,'laund/booking.html')

def pay(request):
 ref=str(uuid.uuid4())
 Order.objects.create(reference=ref,amount=5000)
 return render(request,'laund/paystack.html',{'ref':ref,'amount':500000})
