from django import forms

class InviteForm(forms.Form):
	email = forms.EmailField(
					widget=forms.EmailInput(
						attrs={
							'class': 'form-signin input',
							'placeholder': 'Your e-mail address',
							}),
					label='')