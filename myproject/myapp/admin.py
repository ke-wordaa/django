# myapp/admin.py
from django.contrib import admin
from .models import MyappYourmodel

@admin.register(MyappYourmodel)
class MyappYourmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)



