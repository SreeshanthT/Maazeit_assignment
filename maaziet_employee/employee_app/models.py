from django.db import models

from maaziet_employee.utils import BaseContent

# Create your models here.

class Employee(BaseContent):
    full_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length = 100, null = True)
    phone = models.CharField(max_length = 100, null = True)
    email = models.EmailField()
    
class Department(BaseContent):
    name = models.CharField("Department Name",max_length=100,null=True)
    
class Designations(BaseContent):
    name = models.CharField("Designation",max_length=100,null=True)
    