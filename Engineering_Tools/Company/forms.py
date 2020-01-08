from  django import forms
from .models import Register, Company_Profile

class register_form(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {
            'c_name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'class': 'form-control'}),
            'c_email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'c_password': forms.TextInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
            'c_r_password': forms.TextInput(attrs={'placeholder': 'Enter Confirm Password', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(register_form, self).__init__(*args, **kwargs)
        self.fields['c_name'].label = ''
        self.fields['c_email'].label = ''
        self.fields['c_password'].label = ''
        self.fields['c_r_password'].label = ''



class login_form(forms.ModelForm):
    class Meta:
        model = Register
        fields = [ 'c_email' , 'c_password' ]
        widgets = {
            'c_email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'c_password': forms.TextInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(login_form, self).__init__(*args, **kwargs)
        self.fields['c_email'].label = ''
        self.fields['c_password'].label = ''


class profile_form(forms.ModelForm):
    class Meta:
        model = Company_Profile
        fields = "__all__"
        widgets = {
            'c_name': forms.TextInput(attrs={'class': 'form-control'}),
            'c_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'c_street': forms.TextInput(attrs={'class': 'form-control'}),
            'c_area': forms.TextInput(attrs={'class': 'form-control'}),
            'c_city': forms.TextInput(attrs={'class': 'form-control'}),
            'c_state': forms.TextInput(attrs={'class': 'form-control'}),
            'c_country': forms.TextInput(attrs={'class': 'form-control'}),
            'c_pincode': forms.TextInput(attrs={'class': 'form-control'}),

        }