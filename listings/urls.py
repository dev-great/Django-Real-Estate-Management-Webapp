from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.index , name='listings'),
    path('<int:listing_id>/',views.listing , name='listing'),
    path('search/',views.search , name='search'),

]
