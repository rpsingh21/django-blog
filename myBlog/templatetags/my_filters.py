from django import template
from django.template.loader import get_template

register = template.Library()

@register.simple_tag
def comment_reply(comments,request):
	context = {
		'request':request,
		'comments':comments
	}
	template = get_template('comments/core_comments.html')
	html  = template.render(context)
	return html

@register.filter(name='moduler')
def moduler(value):
	return value%9+1

@register.simple_tag(name='user_activity')
def user_activity(comment, request):
	activity = comment.activitys.filter(user=request.user)
	fav = None
	vote = None
	if activity.filter(activity_type='F').exists():
		fav = 'F'
	if activity.filter(activity_type='U').exists():
		vote = 'U'
	elif activity.filter(activity_type='D').exists():
		vote = 'D'
	return [fav,vote]