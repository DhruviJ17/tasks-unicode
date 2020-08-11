from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
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


def queryuser(request):
    form = parsedData()
    if request.method == 'POST':
        form = parsedData(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return Query(request, username)
    context = {'form': form}
    return render(request, 'acc/user.html', context)


def Query(request, username):
    response = requests.get('https://api.github.com/users/' + username + '/repos')
    response1 = requests.get('https://api.github.com/users/' + username + '/followers')
    name_list = []
    followers_list = []
    username_dict = ApiQuery.objects.all().values('username')
    username_list = []
    for k in username_dict:
        username_list.append(k['username'])

    if response:
        user_data = response.json()
        for i in user_data:
            name_list.append(i['name'])
        repo_count = len(name_list)
        if username in username_list:
            x = ApiQuery.objects.get(username=username)
            x.repo_count = repo_count
            x.save()

    if response1:
        followers_data = response1.json()
        for i in followers_data:
            followers_list.append(i['login'])
        followers_count = len(followers_list)
        if username in username_list:
            x = ApiQuery.objects.get(username=username)
            x.followers_count = followers_count
            x.save()

    context = {'names': name_list, 'followers': followers_list}
    return render(request, 'acc/apiquery.html', context)

def repoQuery(request):
    form = RepoData()
    result = None
    if request.method == 'POST':
        form = RepoData(request.POST)
        if form.is_valid():
            repo_count = form.cleaned_data['repo_count']
            result = ApiQuery.objects.filter(repo_count=repo_count)
            for x in result:
                x.count += 1
                x.save()

    context = {'form': form, 'result': result}
    return render(request, 'acc/repo.html', context)

def foloQuery(request):
    form = FoloData()
    result = None
    if request.method == 'POST':
        form = FoloData(request.POST)
        if form.is_valid():
            followers_count = form.cleaned_data['followers_count']
            result = ApiQuery.objects.filter(followers_count=followers_count)
            for x in result:
                x.count += 1
                x.save()

    context = {'form': form, 'result': result}
    return render(request, 'acc/folo.html', context)


def topthree(request):
    answer = ApiQuery.objects.order_by('count')[:3]
    context = {'answer': answer}
    return render(request, 'acc/top.html', context)






