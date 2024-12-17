from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
