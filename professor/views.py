from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from student.models import first_year, second_year, third_year, Csv
from student.forms import CsvModelForm
from .models import subject
import csv

# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        form = CsvModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            form = CsvModelForm()
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    row = ";".join(row)
                    row = row.replace(";", "  ")
                    row = row.split("  ")
                    
                    rollno = int(row[0])
                    studentName = row[1].upper()
                    enNo = row[2]
                    sem = subject.objects.get(semester=int(row[3]))
                    sub1 = int(row[4])
                    sub2 = int(row[5])
                    sub3 = int(row[6])
                    sub4 = int(row[7])
                    sub5 = int(row[8])
                    sub6 = int(row[9])

                    first_year.objects.create(roll_no=rollno, student_name=studentName, enrollment_no=enNo,
                    semester=sem, sub_1=sub1, sub_2=sub2, sub_3=sub3, sub_4=sub4, sub_5=sub5, sub_6=sub6)

                obj.activated = True
                obj.save()

        return render(request, 'dashboard.html', {'form':form})
    else:
        return render(request, 'login.html')

def handellogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('dashboard')

    return render(request, 'login.html')

def handellogout(request):
    logout(request)
    return redirect('dashboard')
    