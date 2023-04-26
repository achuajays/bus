from django.shortcuts import render , get_object_or_404 , redirect
from .models import bus , reg , log
from .forms import logf , regf , f , rf
import csv
from django.http import HttpResponse

# Create your views here.


def buss(request):
    form = logf(request.POST)
    if form.is_valid():
        form.save()
        return redirect (busv)




    form = logf()
    return render (request,'app/busadd.html',{'form':form})


def busv(request):
    form = bus.objects.all()
    f = request.session['user']
    return render (request ,'app/busview.html',{'f':f,'form':form})


def regs(request , id = id):
    form = regf(request.POST)
    if form.is_valid():
        l = get_object_or_404(bus,id = id)
        name = request.session['user']
        addarno = form.cleaned_data['addarno']
        nos = form.cleaned_data['nos']
        reg(bus = l , name = name , addarno = addarno , nos = nos).save()
        return redirect (busv)
        






    form = regf()
    return render (request,'app/reg.html',{'form':form})


def login(request):
    
    if(request.method == "POST" ):
        form = f(request.POST)
        if (form.is_valid()):

            u=form.cleaned_data['user']
            request.session['user'] = u
            p=form.cleaned_data['password']
            a = log.objects.filter(user = u ,  password = p).first()
            if (a is not None):
                return redirect(busv)
            else:
                return render (request , 'app/login.html' , {'form':form,'key':"not identified "})
    form = f()         

    

                
    

    return render (request , 'app/login.html' , {'form':form,'key':""})







def register(request):
    form = rf(request.POST)
    if form.is_valid():
        form.save()
        return redirect (login)




    form = rf()
    return render (request,'app/register.html',{'form':form})

def ticket(request):
    u = request.session['user']
    form = reg.objects.filter(name = u )
    return render  (request , 'app/ticket.html',{'form':form})



def my_csv_view(request):
    # Query your model data
    queryset = reg.objects.all()

    # Set response headers for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mydata.csv"'

    # Create CSV writer object
    writer = csv.writer(response)

    # Write headers to CSV
    writer.writerow(['BUsName', 'Destination','v_no','Name','Addharr no','Noof seats'])

    # Write data to CSV
    for obj in queryset:
        writer.writerow([obj.bus.name, obj.bus.destination , obj.bus.v_no , obj.name , obj.addarno , obj.nos])

    return response


def my_text_file_view(request ,id =id ):
    # Open the text file
    form = get_object_or_404(reg  , id = id)
    contents = f"""Riding in Comfort: Exploring the World with [Bus Company Name]\n\n\nname = { form.name }\nbus  = { form.bus.name }\ndate = { form.bus.date  }\nnoofs = { form.nos } \n\n\n\n
    A bus company provides transportation services to passengers traveling by bus. The company has a fleet of buses that operate on different routes across various cities. The buses are designed to be comfortable and safe for passengers, with features such as air conditioning, reclining seats, and on-board restrooms. The company also employs trained drivers who are responsible for operating the buses and ensuring the safety of passengers. In addition to regular bus services, the company may also offer charter services for group travel, such as school trips or corporate events. Overall, a bus company is an important part of the transportation infrastructure and provides a convenient and affordable option for passengers to travel to their desired destinations.
    """

    # Set response headers for text file
    response = HttpResponse(contents, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="mytextfile.txt"'

    return response