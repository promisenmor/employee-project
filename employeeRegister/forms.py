from django import forms
from . models import Employee, Position


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('Fullname', 'Emp_code', 'mobile', 'position')
        labels = {
            'Fullname': 'Full Name',
            'Emp_code': 'Emp. code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'select position'