from django.shortcuts import render

# Create your views here.
def appartments(request):
	return render(request, 'appartments.html')