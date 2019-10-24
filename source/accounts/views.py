from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request, **kwargs):
    context = {}
    redirect_url = 'index'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_url = request.POST.get('redirect_url')
        print(redirect_url)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            context['has_error'] = True
    if request.method == 'GET':
        next = request.GET.get('next')
        if next:
            redirect_url = next
    context['redirect_url'] = redirect_url
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')
