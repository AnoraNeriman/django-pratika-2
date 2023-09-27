from django.contrib import admin
from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'level',
        'about',
        'phone',
    )

    list_display = ['name', 'image', 'level', 'about', 'phone']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = (
        'picture',
        'title', 
        'about',
        'vidio',
    )

    list_display = ['picture', 'title', 'about', 'vidio']

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    fields = (
        'fullname',
        'email',
        'number',
        'extnumber',
        'day',
        'stu_day',
    ) 

    list_display = ['fullname', 'email', 'number', 'extnumber', 'day', 'stu_day']

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    fields = (
        'lider',
    )     

    list_display = ['lider']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = (
        'tel_nomer',
        'email',
        'level',
        'message',
    )    

    list_display = ['tel_nomer', 'email', 'level', 'message']