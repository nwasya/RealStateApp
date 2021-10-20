from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from RE_account.forms import LoginForm


def add_user_to_group(username,group_name:str):
    from django.contrib.auth.models import Group
    my_group = Group.objects.get(name=group_name)
    my_group.user_set.add(username)


def login_page(request):

    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)

        user_name = request.POST['user_name']

        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            first_name = request.user.first_name
            last_name = request.user.last_name

            messages.info(request, f" {first_name} {last_name} عزیز ، شما با موفقیت وارد سیستم شدید. .")
            return redirect('/')
        else:
            login_form.add_error('password', 'رمز نا معتبر است.')

    context = {

        'login_form': login_form

    }
    return render(request, 'login_form.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')

