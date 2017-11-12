from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from crispy_forms.utils import render_crispy_form
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from .models import *
from AppControl.models import Profile,UpdateProfileBoxModelForm


#@login_required
def home( request):
	# username,mail = request.user.username.split("@")
	username= request.user.username

	return render(request, 'home.html',{'username':username})

@login_required
def mybox( request):
	try:
		box_list = Box.objects.filter(owner=request.user)
		print (box_list)
		return render(request, 'mybox.html',{'box_list':box_list})
	except Box.DoesNotExist as e:
		messages.error(request, 'คุณยังไม่มีกล่องเห็ด')
	else:
		pass
	finally:
		pass
	
	# box_list = Box.objects.all()
	return render(request, 'mybox.html',)

@login_required
def add_box( request):
	boxform = CreateBoxModelForm()
	if request.method == 'POST':
		# boxform = CreateBoxModelForm(request.POST, request.FILES)
		print(request.POST)
		try:
			code = request.POST.get('code')
			obj = Box.objects.get(code=code)
			box = Box.objects.filter(code=code).update(owner=request.user)

			return redirect('add_box_profile', pk=obj.pk)
		except Box.DoesNotExist:
			messages.error(request, 'ไม่มีหมายเลขนี้อยู่ในระบบ กรุณากรอกใหม่อีกครั้ง')

		# if boxform.is_valid():
		# 	try:
		# 		obj = Box.objects.get(code=boxform.cleaned_data['code'])
		# 		box = Box.objects.filter(code=boxform.cleaned_data['code']).update(owner=request.user)

		# 		return redirect('add_box_profile', pk=obj.pk)
		# 	except Box.DoesNotExist:
		# 		messages.error(request, 'ไม่มีหมายเลขนี้อยู่ในระบบ กรุณากรอกใหม่อีกครั้ง')
			# box = Box.objects.create(
			# 	code=boxform.cleaned_data['code'],
			# 	password = boxform.cleaned_data['password'],
			# 	)


			# return HttpResponseRedirect('/mushroom/mybox')

	return render(request, 'addbox.html',{'boxform':boxform,'user':request.user})

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

	return render(request, 'addprofile.html',{'boxform':boxform})

@login_required
def detail_box(request,pk):
	# username,mail = request.user.username.split("@")
	box_obj = Box.objects.get(id=pk)
	return render(request, 'moredetail.html',{'box_obj':box_obj})
	
	# return render(request, 'moredetail.html',{'username':username})

@login_required
def delete_box(request, pk):

    item = Box.objects.get(id=pk)
    item.delete()
# <!--   <button style="float: right;" class="button btn-default"> <a style="color: black" href="{% url 'delete_box' box.id %}">Delete me</a></button> -->
    return HttpResponseRedirect('/mushroom/mybox')

# @login_required
# def update_box(request, pk):
# 	form = UpdateProfileBoxModelForm()
# 	if request.method == 'POST':
# 		if form.is_valid():

# 	return render(request, 'update.html',{'form':form})
class UpdateBoxView(UpdateView):
    queryset = Box.objects.all()
    template_name='update.html'
    form_class = UpdateProfileBoxModelForm
    success_url = '/mushroom/mybox'
    # item = Box.objects.get(id=pk)
    # item.delete()
# <!--   <button style="float: right;" class="button btn-default"> <a style="color: black" href="{% url 'delete_box' box.id %}">Delete me</a></button> -->
    # return HttpResponseRedirect('/mushroom/mybox')

def buy_box(request):
	buyform = BuyBoxModelForm()
	if request.method == 'POST':
		buyform = BuyBoxModelForm(request.POST, request.FILES)
		if buyform.is_valid():
			buy_obj = Buy.objects.create(
				name=buyform.cleaned_data['name'],
				address = buyform.cleaned_data['address'],
				email = buyform.cleaned_data['email'],
				phone_number = buyform.cleaned_data['phone_number'],
				order_amount = buyform.cleaned_data['order_amount'],
				)
			messages.success(request, 'คุณได้สั่งซื้อเรียบร้อยแล้ว', extra_tags='alert')
			return HttpResponseRedirect('/mushroom/buy/success')
		else:
			print("not valid")
			messages.error(request, "Error")
	return render(request, 'buy.html',{'buyform':buyform})

def contact(request):
	return render(request, 'contact.html')

def buybox_success(request):
	return render(request, 'buybox_success.html')

def buybox( request):
	return render(request, 'buy.html')

def contact( request):
	return render(request, 'contact.html')

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
