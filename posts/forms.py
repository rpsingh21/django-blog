from django import forms

from pagedown.widgets import PagedownWidget
from .models import Posts

# from for create and update post 
class PostForms(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget())
	class Meta:
		model=Posts
		fields =[
			'title',
			'tags',
			'content',
			'image',
		]