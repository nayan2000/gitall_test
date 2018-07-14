from django import forms

from .models import UserAccount

class UserAccountForm(forms.ModelForm):

	class Meta:
		model = UserAccount
		# exclude these from the form as we don't need these to be changed or worked on
		exclude = ('user', 'user_since', 'totos', 'width_field', 'height_field')