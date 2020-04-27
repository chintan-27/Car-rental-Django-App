from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Carrent,Location,RentedCar
from .forms import DateForm,RegisterCar

from .forms import SignUpForm
# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    user = request.user
    c = RentedCar.objects.filter(username_id=user)
    response = {'Cars': c}
    return render(request,'dashboard.html',response)



def registerView(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
            form=SignUpForm()
    return render(request,'registration/register.html',{'form': form})




def rentNow(request):
    form = DateForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            date = form.cleaned_data['date']
            d = {'date':date}
            a=Carrent.objects.all()
            a1 = {'CARS':a}
            f = {'form':form}
            response = {**a1,**f,**d}
            return render(request,'rentnow.html',response)
    else:
        return render(request,'rentnow.html',{'form':form})




@login_required
def carRented(request,id=None,date=None):
    #b=Carrent.objects.get(id=1)
    b=get_object_or_404(Carrent,id=id)
    d = {'date':date}
    b1 = {'Rents':b}
    response = {**b1,**d}
    return render(request,'carrented.html',response)

def loc(request):
    c=Location.objects.all()
    return render(request,'mycars.html',{'LOC':c})

def locs(request,id=None):
    #b=Carrent.objects.get(id=1)
    d=get_object_or_404(Location,id=id)
    return render(request,'bill.html',{'locates':d})

def rented(request,car_num=None,date=None):
    user = request.user
    c =RentedCar.objects.filter(date=date).filter(car_num=car_num)
    if not c:
        b = RentedCar(username_id=user,car_num=car_num,date=date)
        b.save()
        return redirect('loc')
    else:
        return redirect('booked')

def booked(request):
    return render(request,'booked.html')

@login_required
def registerCar(request):
        if request.method=="POST":
            form=RegisterCar(request.POST)
            if form.is_valid():
                car_name = form.cleaned_data['car_name']
                car_color=form.cleaned_data['car_color']
                transmission_type=form.cleaned_data['transmission_type']
                fuel_type=form.cleaned_data['fuel_type']
                costperday = form.cleaned_data['costperday']
                car_num = form.cleaned_data['car_num']
                car_image=form.cleaned_data['car_image']
                z = Carrent(car_name=car_name,car_color=car_color,transmission_type=transmission_type,fuel_type=fuel_type,costperday=costperday,car_num=car_num,car_image=car_image)
                z.save()
                return redirect('dashboard')
            else:
                print(form.errors)
                form=RegisterCar()
                return render(request,'registercar.html',{'form': form})
        else:
            form=RegisterCar()
            return render(request,'registercar.html',{'form': form})
