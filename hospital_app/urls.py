from django.contrib import admin
from django.urls import path
from hospital_app.models import Doctor,Patient,Appointment
from .views import Index, About, Login, logout_admin, Contact, view_doctor, add_doctor, delete_doctor, view_patient, add_patient, delete_patient, view_appt, add_appt, delete_appt


urlpatterns = [
    path('about/',About, name='about'),
    path('contact/',Contact, name='contact'),
    path('',Index,name='home'),
    path('admin_login/',Login, name='login'),
    path('logout_admin/',logout_admin, name='logout_admin'),
    path('view_doctor/',view_doctor, name='view_doctor'),
    path('add_doctor/',add_doctor, name='add_doctor'),
    path('delete_doctor/<int:pid>/',delete_doctor, name='delete_doctor'),
    path('view_patient/',view_patient, name='view_patient'),
    path('add_patient/',add_patient, name='add_patient'),
    path('delete_patient/<int:pid>/',delete_patient, name='delete_patient'),
    path('view_appt/',view_appt, name='view_appt'),
    path('add_appt/',add_appt, name='add_appt'),
    path('delete_appt/<int:pid>/',delete_appt, name='delete_appt'),
]