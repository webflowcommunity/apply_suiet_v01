from django.contrib import admin
from .models import Addmision
# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phono', 'state', 'course')
    list_filter = ('name','state')
    search_fields = ['name', 'state']




admin.site.register(Addmision,CommentAdmin)