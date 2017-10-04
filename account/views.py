from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
)
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
# Create your views here.

def login_view(request):
	form = LoginForm(request.POST or None)
	next = request.GET.get('next')
	if request.method == 'POST':
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user=authenticate(username=username, password=password)
			login(request, user)
			if next:
				return redirect(next)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	return render(request , "login.html",{"title":"Login","form":form});

def register_view(request):
	form = RegisterForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user=form.save(commit=False)
			password = form.cleaned_data.get("password")
			user.set_password(password)
			user.save()
			login(request,user)
			return HttpResponseRedirect('/')
	return render(request , "login.html",{"title":"Register","form":form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
