from django.contrib.auth.forms import AuthenticationForm
from authentication.models import User
from blog.models import Blog
from django import forms
from django.db.models import Q

class EditorAuth(AuthenticationForm):
    class Meta:
        model = User
        
    def __init__(self, *args, **kwargs) -> None:
        super(EditorAuth,self).__init__(*args, **kwargs) 
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        editor_admin = User.objects.filter(Q(is_staff=True) | Q(is_editor=True),email=username)
        print(editor_admin)
        if not editor_admin.exists():
            raise forms.ValidationError("No Editor Avalibale Of This Email Address.")
        return username
    
    
class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','subtitle','post','status',]
        
    def __init__(self, *args, **kwargs): 
        super(BlogCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'status':
                self.fields[field].widget.attrs.update({'class':'form-control'})
            
                
        