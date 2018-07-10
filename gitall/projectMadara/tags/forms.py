from django import forms


from .models import Tag

class TagForm(forms.ModelForm):
	# content = forms.CharField(widget=PagedownWidget)
	class Meta:
		model = Tag
		fields = ('text',)
