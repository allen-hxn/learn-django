from django.contrib import admin
from .models import Person

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'age']

admin.site.register(Person)