from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from . import Check
from .models import *
from .forms import *

def home(request):

    return render(request, 'acc/main.html')

def solutionform(request):
    form = NumForm()
    if request.method == "POST":
        form = NumForm(request.POST)
        if form.is_valid:
            form.save()
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return solution(request, num1, num2)

    context = {'form': form}
    return render(request, 'acc/forms.html', context)


def solution(request, num1, num2):
    dict = Check.Check(num1, num2)
    context = {'dict': dict}
    return render(request, 'acc/solution.html', context)
