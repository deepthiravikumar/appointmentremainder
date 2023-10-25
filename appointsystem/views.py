from django.shortcuts import render, redirect
from .models import userregister
from django.http import HttpResponse
from django.template import loader

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userregister.objects.create(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = userregister.objects.filter(username=username, password=password).first()
        if user:
            return redirect('homepage.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def homepage(request):
    template=loader.get_template('homepage.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def signup(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render())
