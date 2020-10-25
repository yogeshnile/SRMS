from django.contrib import admin
from .models import first_year, second_year, third_year, Csv
from .resources import FirstResource, SecoundResource, ThirdResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(first_year)
class FirstAdmin(ImportExportModelAdmin):
    resource_class = FirstResource
    list_display = ('roll_no','student_name','enrollment_no','semester','sub_1','sub_2','sub_3',
        'sub_4','sub_5','sub_6',)
    list_display_links = ('roll_no','student_name',)
    search_fields = ('roll_no','student_name','enrollment_no')
    list_per_page = 50

@admin.register(second_year)
class SecoundAdmin(ImportExportModelAdmin):
    resource_class = SecoundResource
    list_display = ('roll_no','student_name','enrollment_no','semester','sub_1','sub_2','sub_3',
        'sub_4','sub_5','sub_6',)
    list_display_links = ('roll_no','student_name',)
    search_fields = ('roll_no','student_name','enrollment_no')
    list_per_page = 50

@admin.register(third_year)
class ThirdAdmin(ImportExportModelAdmin):
    resource_class = ThirdResource
    list_display = ('roll_no','student_name','enrollment_no','semester','sub_1','sub_2','sub_3',
        'sub_4','sub_5','sub_6',)
    list_display_links = ('roll_no','student_name',)
    search_fields = ('roll_no','student_name','enrollment_no')
    list_per_page = 50
    
admin.site.register(Csv)
