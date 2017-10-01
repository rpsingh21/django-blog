from django import template
from django.template.loader import get_template

register = template.Library()

@register.filter(name='comment_reply')
def comment_reply(comments):
	context = {
		'comments':comments
	}
	template = get_template('comments.html')
	html  = template.render(context)
	return html

@register.filter(name='moduler')
def moduler(value):
	return value%8+1