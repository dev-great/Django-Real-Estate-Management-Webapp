from django.db import models
from datetime import datetime

# Create your models here.
class AgesVerification(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	upload_date = models.DateTimeField(default=datetime.now() , blank=True)
	upload_file = models.FileField(upload_to='documents/')

	def __str__(self):
		return self.name