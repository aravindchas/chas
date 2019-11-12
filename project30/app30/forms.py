from django import forms

class EmployeeForm(forms.Form):
    f_idno=forms.IntegerField()
    f_name=forms.CharField()
    f_sal=forms.FloatField()