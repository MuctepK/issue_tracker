from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.forms import SignUpForm


def login_view(request, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'register.html', context={'form':form})
    elif request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            activation_url = reverse('accounts:user_activate',kwargs={'pk':user.pk})
            user.email_user('Вы зарегистрировались на сайте localhost:8000',
                            'Для активации перейдите по ссылке: ' + activation_url)
            return redirect('index')
        else:
            return render(request, 'register.html', context={'form': form})


def user_activation_view(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('index')
