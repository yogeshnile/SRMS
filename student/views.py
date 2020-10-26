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

        if year == '1st Year':
            student = first_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')
        elif year == '2nd Year':
            student = second_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')
        elif year == '3rd Year':
            student = third_year.objects.filter(roll_no = roll_no).first()
            if student is None:
                messages.error(request, f"Roll no:- {roll_no} Result has not published yet.")
                return redirect('home')
        
        context = {
            'sub':student,
        }
        return render(request, 'result.html', context)

    return redirect('home')
