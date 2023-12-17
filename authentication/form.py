from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class UserCreateFm(UserCreationForm):
    password2 = forms.CharField(label="Confrim Password")
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    
    def __init__(self, *args, **kwargs):
        super(UserCreateFm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
class UserLoginFm(AuthenticationForm):
    class Meta:
        model = User
    
    def __init__(self, *args, **kwargs):
        super(UserLoginFm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    

        