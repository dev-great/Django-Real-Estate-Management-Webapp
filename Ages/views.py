from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AgesVerification
from .forms import AgesVerificationForm
from django.contrib import messages

# Create your views here.
def model_form_upload(request):
	if request.method == "POST":
		form = AgesVerificationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'Your Request has Been Submitted')
			return redirect('pages:index')

	else:
		form = AgesVerificationForm()
	return render(request, 'pages/agesverification.html', {'form' : form},)