from django import forms

from employee_app.models import *

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control',
                'placeholder':self.fields[name].label,
            })
    
    class Meta:
        model = Employee
        fields = ['full_name','last_name','phone','email']
        
    def clean_phone(self):
        import re
        self.cleaned_data
        phone_regex = "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
        phone = self.cleaned_data.get("phone")
        if not re.match(phone_regex,phone):
            raise forms.ValidationError("Invalid Phone number")
        return phone