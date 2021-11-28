from django import forms
from .models import AgesVerification


class AgesVerificationForm(forms.ModelForm):

	class Meta:
		model = AgesVerification
		fields = ('name', 'email', 'phone', 'upload_file',)
