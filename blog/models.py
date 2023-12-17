from django.db import models
from tinymce.models import HTMLField
from authentication.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(max_length=400, null=True,blank=True)
    slug = models.SlugField(max_length=200,unique=True)
    post = HTMLField()
    status = models.BooleanField(help_text="Check For Active else Inactive",default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'is_staff': True})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
class EditorForm(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'is_staff': False})
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=550)
    portfolio_url = models.URLField(max_length=500, verbose_name="Any URL", null=True, blank=True)
    resume = models.ImageField(upload_to='resume/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.subject