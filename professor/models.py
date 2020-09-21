from django.db import models
from django.utils.timezone import now

# Create your models here.

class subject(models.Model):
    sno = models.AutoField(primary_key=True)
    SEMESTER_CHOICES = [
        (1, '1st'),
        (2, '2nd'),
        (3, '3rd'),
        (4, '4th'),
        (5, '5th'),
        (6, '6th'),
    ]
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    sub_1 = models.CharField(max_length=50)
    sub_2 = models.CharField(max_length=50)
    sub_3 = models.CharField(max_length=50)
    sub_4 = models.CharField(max_length=50)
    sub_5 = models.CharField(max_length=50)
    sub_6 = models.CharField(max_length=50, null=True)
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return "semester " + str(self.semester)