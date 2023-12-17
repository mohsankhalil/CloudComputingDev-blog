from .models import EditorForm, Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']
        
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EditorFM(forms.ModelForm):
    class Meta:
        model = EditorForm
        fields = ['subject','message','portfolio_url','resume']
        enctype= "multipart/form-data"
    
    def __init__(self, *args, **kwargs):
        super(EditorFM, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})