from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from crispy_forms.utils import render_crispy_form

@login_required
def home( request):
	return render(request, 'home.html')

def add_box( request):
	return render(request, 'addbox.html')