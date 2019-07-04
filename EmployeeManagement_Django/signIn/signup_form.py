from django import forms

class Signup_Form(forms.Form):
    name = forms.CharField(label = "Enter Name")
    age = forms.DecimalField(label = "Enter Age")
    designation = forms.CharField(label = "Enter Designation")
    experience = forms.CharField(label = "Enter Experience")
    emailId = forms.EmailField(label = "Enter Email")
    password = forms.CharField(label = "Enter Password")
