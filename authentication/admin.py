from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class userItems(admin.ModelAdmin):
    model = User
    list_display = ('email','name', 'is_editor','is_staff', 'is_active',)
    list_filter = ('first_name','email', 'is_editor','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_editor',
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name','email', 'password1', 'password2','is_editor',)
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    def name(self, obj):
        if obj.last_name is None:
            return obj.first_name
        return '{} {}'.format(obj.first_name, obj.last_name)