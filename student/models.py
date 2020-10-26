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
    total_marks = models.IntegerField(default=0)
    percentage = models.CharField(max_length=10, default="-")
    result = models.CharField(max_length=4, default="FAIL")
    timeStamp = models.DateTimeField(default=now, blank=True)

    def save(self, *args, **kwargs):
        self.total_marks = self.sub_1+self.sub_2+self.sub_3+self.sub_4+self.sub_5+self.sub_6
        if self.sub_1<35 or self.sub_2<35 or self.sub_3<35 or self.sub_4<35 or self.sub_5<35 or self.sub_6<70:
            self.result = "FAIL"
            self.percentage = "-"
        else:
            self.result = "PASS"
            self.percentage = str(round((self.total_marks * 100)/700, 2)) + " %"
        super().save(*args, **kwargs)

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
    total_marks = models.IntegerField(default=0)
    percentage = models.CharField(max_length=10, default="-")
    result = models.CharField(max_length=4, default="FAIL")
    timeStamp = models.DateTimeField(default=now, blank=True)

    def save(self, *args, **kwargs):
        self.total_marks = self.sub_1+self.sub_2+self.sub_3+self.sub_4+self.sub_5+self.sub_6
        if self.sub_1<35 or self.sub_2<35 or self.sub_3<35 or self.sub_4<35 or self.sub_5<35 or self.sub_6<70:
            self.result = "FAIL"
            self.percentage = "-"
        else:
            self.result = "PASS"
            self.percentage = str(round((self.total_marks * 100)/700, 2)) + " %"
        super().save(*args, **kwargs)

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
    total_marks = models.IntegerField(default=0)
    percentage = models.CharField(max_length=10, default="-")
    result = models.CharField(max_length=4, default="FAIL")
    timeStamp = models.DateTimeField(default=now, blank=True)

    def save(self, *args, **kwargs):
        if self.semester == 5:
            self.total_marks = self.sub_1+self.sub_2+self.sub_3+self.sub_4+self.sub_5+self.sub_6
            if self.sub_1<35 or self.sub_2<35 or self.sub_3<35 or self.sub_4<35 or self.sub_5<35 or self.sub_6<70:
                self.result = "FAIL"
                self.percentage = "-"
            else:
                self.result = "PASS"
                self.percentage = str(round((self.total_marks * 100)/700, 2)) + " %"
        elif self.semester == 6:
            self.total_marks = self.sub_1+self.sub_2+self.sub_3+self.sub_4
            if self.sub_1<35 or self.sub_2<35 or self.sub_3<150 or self.sub_4<35:
                self.result = "FAIL"
                self.percentage = "-"
            else:
                self.result = "PASS"
                self.percentage = str(round((self.total_marks * 100)/700, 2)) + " %"
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.roll_no) + " " + self.student_name

