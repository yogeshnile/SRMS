from .models import first_year, second_year, third_year
from import_export import resources

class FirstResource(resources.ModelResource):
    class Meta:
        model = first_year
        exclude = ('id', 'timeStamp')
        import_id_fields = ['roll_no']

class SecoundResource(resources.ModelResource):
    class Meta:
        model = second_year
        exclude = ('id', 'timeStamp')
        import_id_fields = ['roll_no']

class ThirdResource(resources.ModelResource):
    class Meta:
        model = third_year
        exclude = ('id', 'timeStamp')
        import_id_fields = ['roll_no']
