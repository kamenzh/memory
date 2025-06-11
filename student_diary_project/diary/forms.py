from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Grade, Absence

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['subject', 'grade']

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['date', 'reason']
