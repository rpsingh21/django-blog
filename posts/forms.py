from django import forms
from markdownx.fields import MarkdownxFormField

from .models import Posts

# from for create and update post 
class PostForms(forms.ModelForm):
	content = MarkdownxFormField()
	class Meta:
		model=Posts
		fields =[
			'title',
			'tags',
			'content',
			'image',
			'draft',
		]