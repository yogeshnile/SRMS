from django.contrib import admin
from .models import subject

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('semester','sub_1','sub_2','sub_3','sub_4','sub_5','sub_6')
    list_filter = ('semester',)
    search_fields = ('semester','sub_1','sub_2','sub_3','sub_4','sub_5','sub_6')

admin.site.register(subject, SubjectAdmin)