from django import forms
from registration.forms import RegistrationForm

class CustomForm(RegistrationForm):
    confirm = forms.CharField(label="First 5 characters of e-mail")
    
    def clean(self):
        data = super(CustomForm, self).clean()
	email = data.get('email')[:5]
        confirm = data.get('confirm')
        if email != confirm :
            raise forms.ValidationError("You did not enter the first 5 characters of your e-mail correctly.")
        return data
	
