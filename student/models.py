from django.db import models
from django.utils.timezone import now
from professor.models import subject

# Create your models here.

class first_year(models.Model):
    sno = models.AutoField(primary_key=True)
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    enrollment_no = models.CharField(max_length=20)
    semester = models.ForeignKey(subject, on_delete=models.CASCADE)
    sub_1 = models.IntegerField(default=0)
    sub_2 = models.IntegerField(default=0)
    sub_3 = models.IntegerField(default=0)
    sub_4 = models.IntegerField(default=0)
    sub_5 = models.IntegerField(default=0)
    sub_6 = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return str(self.roll_no) + " " + self.student_name

class second_year(models.Model):
    sno = models.AutoField(primary_key=True)
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    enrollment_no = models.CharField(max_length=20)
    semester = models.ForeignKey(subject, on_delete=models.CASCADE)
    sub_1 = models.IntegerField(default=0)
    sub_2 = models.IntegerField(default=0)
    sub_3 = models.IntegerField(default=0)
    sub_4 = models.IntegerField(default=0)
    sub_5 = models.IntegerField(default=0)
    sub_6 = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return str(self.roll_no) + " " + self.student_name

class third_year(models.Model):
    sno = models.AutoField(primary_key=True)
    roll_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    enrollment_no = models.CharField(max_length=20)
    semester = models.ForeignKey(subject, on_delete=models.CASCADE)
    sub_1 = models.IntegerField(default=0)
    sub_2 = models.IntegerField(default=0)
    sub_3 = models.IntegerField(default=0)
    sub_4 = models.IntegerField(default=0)
    sub_5 = models.IntegerField(default=0)
    sub_6 = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return str(self.roll_no) + " " + self.student_name