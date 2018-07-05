from django import forms

# Pagedown widget
from pagedown.widgets import PagedownWidget

# Medium text editor
from mediumeditor.widgets import MediumEditorTextarea

from .models import Toto

class TotoForm(forms.ModelForm):
	# content = forms.CharField(widget=PagedownWidget)
	class Meta:
		model = Toto
		fields = ('draft','cover_photo','title','content')

		widgets = {
			'content' : MediumEditorTextarea(attrs={'class':'content'}),
		}
