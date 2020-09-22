from django.shortcuts import render, redirect
from django.contrib import messages
from professor.models import subject
from .models import first_year, second_year, third_year

# Create your views here.
def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        year = request.POST['year']
        roll_no = int(request.POST['roll_no'])

        if year == "Please choose Year" or roll_no == '0':
            messages.error(request, "Please choose option carefully")
            return redirect('home')
        
        def passing(get_object):
            total = get_object.sub_1 + get_object.sub_2 + get_object.sub_3 + get_object.sub_4 + get_object.sub_5 + get_object.sub_6
            if get_object.sub_1 <35 or get_object.sub_2 <35 or get_object.sub_3 <35 or get_object.sub_4 <35 or get_object.sub_5 <35 or get_object.sub_6 <70:
                return "FAIL", "-", total
            else:
                st_grade = round((total*100)/700,2)
                st_grade = str(st_grade) + " %"
                return "PASS", st_grade, total

        if year == '1st Year':
            student = first_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')
            student_result , grade, total = passing(student)
        elif year == '2nd Year':
            student = second_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')
            student_result , grade, total = passing(student)
        elif year == '3rd Year':
            student = third_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')

            if student.semester.sno == 6:
                total = student.sub_1 + student.sub_2 + student.sub_3 + student.sub_4
                if student.sub_1 <35 or student.sub_2 <35 or student.sub_3 <150 or student.sub_4 <35:
                    student_result = "FAIL"
                    grade = "-"
                else:
                    st_grade = round((total*100)/700,2)
                    st_grade = str(st_grade) + " %"
                    student_result = "PASS"
                    grade = st_grade
            else:
                student_result , grade, total = passing(student)
        
        context = {
            'sub':student,
            'student_result':student_result,
            'grade':grade,
            'total':total,
        }
        return render(request, 'result.html', context)

    return redirect('home')

def login(request):
    return render(request, 'login.html')