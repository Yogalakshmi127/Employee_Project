from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from employee_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('', lambda request: redirect('signup/')), 
]
