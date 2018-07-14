from django import forms
from .models import *

from mediumeditor.widgets import MediumEditorTextarea



class WikiAddForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Title', 'class':'form-control','style':'height:100px'}))
    content = forms.CharField(required=True, widget=MediumEditorTextarea(attrs={'placeholder':'Description', 'class':'form-control','style':'height:100px'}))
    history = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'History', 'class':'form-control','style':'height:100px'}))
    features = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'Features', 'class':'form-control','style':'height:100px'}))
    version_history = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'Version', 'class':'form-control','style':'height:100px'}))
    url = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'URL', 'class':'form-control','style':'height:100px'}))
    tech_name = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'Technology Name', 'class':'form-control','style':'height:100px'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder':'http://example.com', 'class':'form-control','style':'height:100px'}))
    eli = forms.CharField(required=False, widget=MediumEditorTextarea(attrs={'placeholder':'ELI', 'class':'form-control','style':'height:100px'}))

    class Meta:
        model = Wiki
        fields = [
            'title',
            'content',
            'history',
            'features',
            'version_history',
            'url',
            'tech_name',
            'website',
            'eli',
        ]

class AddTagsForm(forms.ModelForm):
	class Meta:
		model = Wiki
		fields = ('tags', )

class WikiResourceForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Subject', 'class':'form-control', 'style':'resize:none'}))
    link = forms.URLField(required=False, widget=forms.URLInput(attrs={'placeholder':'http://example.com', 'class':'form-control'}))
    # resource = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Description', 'class':'form-control', 'style':'width:px;resize:none'}))
    resource = forms.CharField(required=True, widget=(MediumEditorTextarea(attrs={'class': 'resource form-control','style':'height:1000px'})))

    class Meta:
        model = Resources
        fields = [
            'title',
            'link',
            'resource'
        ]
