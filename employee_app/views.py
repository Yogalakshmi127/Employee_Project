from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def signup(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enquiry')
    else:
        form = EmployeeForm()
    return render(request, 'signup.html', {'form': form})

def enquiry(request):
    employee = None
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            employee = None
    return render(request, 'enquiry.html', {'employee': employee})
