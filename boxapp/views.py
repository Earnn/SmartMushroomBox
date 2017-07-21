from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from crispy_forms.utils import render_crispy_form
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect,HttpResponse
from .models import *

@login_required
def home( request):
	return render(request, 'home.html')

@login_required
def mybox( request):
	box_list = Box.objects.all()
	return render(request, 'mybox.html',{'box_list':box_list})

@login_required
def add_box( request):
	boxform = CreateBoxModelForm()
	if request.method == 'POST':
		boxform = CreateBoxModelForm(request.POST, request.FILES)

		if boxform.is_valid():
			box = Box.objects.create(
				code=boxform.cleaned_data['code'],
				password = boxform.cleaned_data['password'],
				)
			print ("box: ",box.pk)
			return redirect('add_box_profile', pk=box.pk)
			# return HttpResponseRedirect('/mushroom/mybox')

	return render(request, 'addbox.html',{'boxform':boxform,})

@login_required
def add_box_profile(request, pk):
	boxform = AddProfileBoxModelForm()
	print ("box: ",pk)
	if request.method == 'POST':
		boxform = AddProfileBoxModelForm(request.POST, request.FILES)

		if boxform.is_valid():
			box_update = Box.objects.filter(id=pk).update(name=boxform.cleaned_data['name'],profile=boxform.cleaned_data['profile'])

			print ("box: ",box_update)
			return HttpResponseRedirect('/mushroom/mybox')

	return render(request, 'addprofile.html',{'boxform':boxform,})


@login_required
def delete_box(request, pk):

    item = Box.objects.get(id=pk)
    item.delete()

    return HttpResponseRedirect('/mushroom/mybox')
