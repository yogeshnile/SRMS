from django.contrib import admin
from .models import first_year, second_year, third_year, Csv

# Register your models here.
admin.site.register(first_year)
admin.site.register(second_year)
admin.site.register(third_year)
admin.site.register(Csv)