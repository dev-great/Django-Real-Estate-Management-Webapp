from django.shortcuts import render,redirect

from listings.choices import price_choices , bedroom_choices , state_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True);
	return render(request , 'pages/index.html',{'listings' : listings ,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,

		})


def about(request):
	realtors = Realtor.objects.order_by('-hire_date')
	mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
	context = {
	   'realtors' : realtors,
	   'mvp_realtors' : mvp_realtors
	}
	return render(request , 'pages/about.html',context)
