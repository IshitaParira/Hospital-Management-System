from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from .models import Doctor, Patient, Appointment

# Create your views here.
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    total_doctors = Doctor.objects.all().count()
    total_patients=Patient.objects.all().count()
    total_appt=Appointment.objects.all().count()
    d1={'d':total_doctors,'p':total_patients,'a':total_appt}
    return render(request, 'index.html',d1)

def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'adminlogin.html',d)

def About(request):
    return render(request, 'about.html')

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Contact(request):
    return render(request, 'contact.html')

#VIEWS FOR DOCTOR
def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']
        try:
            Doctor.objects.create(name=n,number=c,special=sp)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'add_doctor.html',d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

#VIEWS FOR PATIENT
def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    p={'pat':pat}
    return render(request,'view_patient.html',p)

def add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        a=request.POST['age']
        g=request.POST['gender']
        num=request.POST['number']
        add=request.POST['address']
        try:
            Patient.objects.create(name=n,age=a,gender=g,number=num,address=add)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'add_patient.html',d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

#VIEWS FOR APPOINTMENT
def view_appt(request):
    if not request.user.is_staff:
        return redirect('login')
    appt=Appointment.objects.all()
    a={'appt':appt} #this 'appt' is used in- {% for i in appt%}
    return render(request,'view_appt.html',a)

def add_appt(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    #this doctor1 is from {% for i in doctor %},it is used to fetch data from Doctor model
    doctor1 = Doctor.objects.all() 
    #this patient1 is from {% for i in patient %}, it is used to fetch data from Patient model
    patient1=Patient.objects.all() 
    if request.method=='POST':
        dn=request.POST['doctor']
        pn=request.POST['patient']
        d=request.POST['date']
        t=request.POST['time']
        # above doctor, patient, date, and time are the names that we gave in the add_appt form
        doctor=Doctor.objects.filter(name=dn).first()
        patient=Patient.objects.filter(name=pn).first()
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d,time1=t)
            error="no"
        except:
            error="yes"
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request, 'add_appt.html',d)

def delete_appt(request,pid):
    if not request.user.is_staff:
        redirect('login')
    app=Appointment.objects.get(id=pid)
    app.delete()
    return redirect('view_appt')