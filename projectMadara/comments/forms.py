"""
   A Form class describes a form and determines how it works and appears.
"""
from django import forms



class CommentForm(forms.Form):
    """
        it is the  form class for our comment system
    """
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea)
