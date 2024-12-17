from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('enquiry/', views.enquiry, name='enquiry'),
]
