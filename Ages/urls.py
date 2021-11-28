from django.urls import path
from . import views
from Ages.views import model_form_upload


app_name = 'Ages'

urlpatterns = [
    path('', model_form_upload, name='Ages'),

]
