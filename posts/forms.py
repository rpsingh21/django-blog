from django import forms

from .models import Posts

# from for create and update post 
class PostForms(forms.ModelForm):
	class Meta:
		model=Posts
		fields =[
			'title',
			'tag',
			'content',
			'image',
		]