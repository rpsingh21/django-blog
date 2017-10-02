from django import template
from django.template.loader import get_template

register = template.Library()

@register.simple_tag
def comment_reply(comments,request):
	context = {
		'request':request,
		'comments':comments
	}
	template = get_template('comments.html')
	html  = template.render(context)
	return html

@register.filter(name='moduler')
def moduler(value):
	return value%9+1