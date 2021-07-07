from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth

from contacts.models import Contact
from django.contrib.auth.models import User



# Create your views here.
def register_view(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password == password2:
			if User.objects.filter(username=username).exists():
					messages.error(request , 'User Name Already Taken')
					return redirect('accounts:register_view')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(request , 'Email Name Already Exits ')
					return redirect('accounts:register_view')
				else:
					user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name
						=last_name)
					# auth.login(request , user)
					# messages.success(request,'You Are Now LoggedIn')
					# return redirect('pages:index')
					user.save()
					messages.success(request,'You Are Now Registered')
					return redirect('accounts:login_view')
		else:
			messages.error(request , 'Password Doest Not Match')
			return redirect('accounts:register_view')

	else:
		return render(request,'accounts/register.html')


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username , password=password)
		if user is not None:
			auth.login(request,user)
			messages.success(request,'You Are Now LoggedIn')
			return redirect('accounts:dashborad')
		else:
			messages.error(request,'Invalid Credentials')
			return redirect('accounts:login_view')
	else:
		return render(request,'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request,'You Are Now Logged Out')
		return redirect('pages:index')


def dashborad(request):
	user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	return render(request,'accounts/dashborad.html',{'contacts' : user_contact})
