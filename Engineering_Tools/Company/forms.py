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


class add_profile_form(forms.ModelForm):
    class Meta:
        model = Company_Profile
        fields = ['c_phone','c_street', 'c_area', 'c_city', 'c_state', 'c_country', 'c_pincode', 'c_website', 'c_linkedin', 'c_logo']
        widgets = {
            'c_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'c_street': forms.TextInput(attrs={'class': 'form-control'}),
            'c_area': forms.TextInput(attrs={'class': 'form-control'}),
            'c_city': forms.TextInput(attrs={'class': 'form-control'}),
            'c_state': forms.TextInput(attrs={'class': 'form-control'}),
            'c_country': forms.TextInput(attrs={'class': 'form-control'}),
            'c_pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'c_website': forms.TextInput(attrs={'class': 'form-control'}),
            'c_linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            'c_logo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(add_profile_form, self).__init__(*args, **kwargs)
        self.fields['c_phone'].label = 'Phone '
        self.fields['c_street'].label = 'Street '
        self.fields['c_area'].label = 'Area '
        self.fields['c_city'].label = 'City '
        self.fields['c_state'].label = 'State '
        self.fields['c_country'].label = 'Country '
        self.fields['c_pincode'].label = 'Pincode '
        self.fields['c_website'].label = 'Website '
        self.fields['c_linkedin'].label = 'Linked-in '
        self.fields['c_logo'].label = 'Logo'


class forgot_password_form(forms.Form):
    email = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}),)

    def __init__(self, *args, **kwargs):
        super(forgot_password_form, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''


class otp_match_form(forms.Form):
    otp = forms.CharField(max_length = 6, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your OTP'}))

    def __init__(self, *args, **kwargs):
        super(otp_match_form, self).__init__(*args, **kwargs)
        self.fields['otp'].label = ''


class add_new_password_form(forms.ModelForm):
    class Meta:
        model = Register
        fields = [ 'c_password' , 'c_r_password' ]
        widgets = {
            'c_password': forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'c_r_password': forms.TextInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(add_new_password_form, self).__init__(*args, **kwargs)
        self.fields['c_password'].label = ''
        self.fields['c_r_password'].label = ''
