from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse

from sqliteqs.config import sql_con,dict_factory
from maaziet_employee.utils import get_objects_or_none
from employee_app.models import Employee
from employee_app.forms import EmployeeForm

import datetime

# Create your views here.

def index(request,**kwargs):
    messages.success(request,'hi')
    # modified_on = created_on = datetime.datetime.now()
    # sql_con.row_factory = dict_factory
    # cur = sql_con.cursor()
    # print(dir(cur))
    # cur.execute(
    #     f"""INSERT INTO employee_app_employee
    #         ('active','modified_on','created_on','full_name','last_name','phone','email') VALUES
    #         ('1','{modified_on}','{created_on}','{'sreeshanth'}','{'T'}','{'9895867939'}','{'sreeshanth@gmail.com'}')
    #     """
    # )
    # sql_con.commit()
    
    # employees = cur.execute("SELECT * FROM employee_app_employee")
    
    # print(employees.fetchone())
    return render(request,'index_page.html',locals())

def employee_manage(request,**kwargs):
    employee = get_objects_or_none(Employee,id=kwargs.get('pk'))
    form = EmployeeForm(instance = employee)
    nav_item = 'employee_nav'
    
    form_title = "Create Employee" if employee is None else f"Update Employee | {employee}"
    
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance = employee)
        modified_on = created_on = datetime.datetime.now()
        full_name,last_name,phone,email = request.POST.get('full_name'),request.POST.get('last_name'),request.POST.get('phone'),request.POST.get('email')
        if form.is_valid():
            if employee is None:
                cur = sql_con.cursor()
                cur.execute(
                    f"""INSERT INTO employee_app_employee 
                        ('active','modified_on','created_on','full_name','last_name','phone','email') VALUES 
                        ('1','{modified_on}','{created_on}','{full_name}','{last_name}','{phone}','{email}')
                    """
                )
                sql_con.commit()
                messages.success(request,'Successfully created')
            else:
                cur = sql_con.cursor()
                cur.execute(
                    f"""UPDATE employee_app_employee SET modified_on='{modified_on}' , 
                    full_name='{full_name}', last_name='{last_name}', phone='{phone}', email='{email}'
                    WHERE id = '{employee.id}'
                    """
                )
                sql_con.commit()
                messages.success(request,'Successfully created')
            return redirect('list-employee')
    
    return render(request,'manage_employee.html',locals())

def employees_list(request):
    sql_con.row_factory = dict_factory
    cur = sql_con.cursor()
    page_context = {"Dashboard":reverse('index_page')}
    page_header = "Employees List"
    employees = cur.execute("SELECT * FROM employee_app_employee").fetchall()
    return render(request,'list_employees.html',locals())