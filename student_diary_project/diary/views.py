from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, GradeForm, AbsenceForm
from .models import Grade, Absence

def home(request):
    return render(request, 'diary/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'diary/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'diary/login.html', {'error': 'Invalid credentials'})
    return render(request, 'diary/login.html')

@login_required
def grades(request):
    grades = Grade.objects.filter(user=request.user)
    return render(request, 'diary/grades.html', {'grades': grades})

@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.user = request.user
            grade.save()
            return redirect('grades')
    else:
        form = GradeForm()
    return render(request, 'diary/add_grade.html', {'form': form})

@login_required
def absences(request):
    absences = Absence.objects.filter(user=request.user)
    return render(request, 'diary/absences.html', {'absences': absences})

@login_required
def add_absence(request):
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            absence.user = request.user
            absence.save()
            return redirect('absences')
    else:
        form = AbsenceForm()
    return render(request, 'diary/add_absence.html', {'form': form})
