from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import Todo
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm,
    TodoForm
)


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todo-home', args=[request.user.username]))
    return render(request, "todo/welcome.html", {'title': 'Home'})


def base(request):
    return render(request, "todo/base.html")


def offline(request):
    return render(request, "todo/offline.html", {'title': 'Offline'})


@login_required(redirect_field_name=None)
def dashboard(request, username):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            add_todo = form.save(commit=False)
            add_todo.user = request.user
            add_todo.save()
            messages.success(
                request, 'Todo has been <strong>added</strong> successfully!')
            return HttpResponseRedirect(reverse('todo-home', args=[username]))
    else:
        form = TodoForm()

    context = {
        'todos': request.user.todo_set.all().order_by('-created_at'),
        'title': 'TodoApp',
        'form': form
    }
    return render(request, "todo/home.html", context)


@login_required
def delete(request, username, pk):
    instance = request.user.todo_set.filter(id=pk)
    instance.delete()
    messages.success(
        request, 'Todo has been <strong>deleted</strong> successfully!')
    return HttpResponseRedirect(reverse('todo-home', args=[username]))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todo-home', args=[request.user.username]))
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # sign_up = form.save(commit=False)
            # sign_up.password = make_password(form.cleaned_data.get('password'))
            # sign_up.status = 1
            # sign_up.save()
            form.save()
            messages.success(
                request, 'User has been <strong>created</strong> successfully!')
            return redirect('user-login')
    else:
        form = RegisterForm()
    return render(request, "todo/register.html", {'form': form, 'title': 'Register'})


@login_required
def handleLogin(request):
    username = request.user.username
    messages.success(
        request, f'Hi <strong>{username}</strong> here are your todos')
    return HttpResponseRedirect(
        reverse('todo-home',
                args=[request.user.username]
                )
    )
