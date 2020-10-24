from django.contrib import admin
from .models import first_year, second_year, third_year, Csv

# Register your models here.
class FirstAdmin(admin.ModelAdmin):
    list_display = (
        'roll_no',
        'student_name',
        'enrollment_no',
        'semester',
        'sub_1',
        'sub_2',
        'sub_3',
        'sub_4',
        'sub_5',
        'sub_6',
    )
    list_display_links = (
        'roll_no',
        'student_name',
    )
    search_fields = (
        'roll_no',
        'student_name',
        'enrollment_no',
    )

admin.site.register(first_year, FirstAdmin)
admin.site.register(second_year, FirstAdmin)

admin.site.register(third_year, FirstAdmin)
admin.site.register(Csv)