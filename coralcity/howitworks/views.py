from django.shortcuts import render

# Create your views here.
def howitworks(request):
	return render(request, 'howitworks.html')