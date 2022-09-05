from django.shortcuts import render

from sqliteqs.config import sql_con,dict_factory
from maaziet_employee.utils import get_objects_or_none
from employee_app.models import Employee

import datetime

# Create your views here.

def index(request,**kwargs):
    modified_on = created_on = datetime.datetime.now()
    sql_con.row_factory = dict_factory
    cur = sql_con.cursor()
    cur.execute(
        f"""INSERT INTO employee_app_employee
            ('active','modified_on','created_on','display_order','full_name','last_name','phone','email') VALUES
            ('1','{modified_on}','{created_on}','{0}','{'sreeshanth'}','{'T'}','{'9895867939'}','{'sreeshanth@gmail.com'}')
        """
    )
    sql_con.commit()
    
    employees = cur.execute("SELECT * FROM employee_app_employee")
    
    print(employees.fetchone())

    return render(request,'index_page.html',locals())

def employee_manage(request,**kwargs):
    employee = get_objects_or_none(Employee,id=kwargs.get('pk'))
    
    if employee is None:
        pass
    else:
        pass
    
    return render(request,'manage_employees.html',locals())

