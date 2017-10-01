from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import  Comments
from .forms import CommentForm

# Create your views here.

def instance_comments(request,object_id):
	comments = Comments.objects.all().filter(object_id=object_id).distinct().order_by('timestamp')
	context = {
		'comments':comments
	}
	return render(request,'comments.html',context)

def reply_form(request,slug,parent_id):
	initial_data = {
		"content_type": "posts",
		"slug": slug,
		"parent_id":parent_id,
	}
	comment_form = CommentForm(request.POST or None,initial=initial_data)
	context ={
		'comment_form':comment_form
	}
	return render(request,'reply_form.html',context)

def comment_delete(request,id):
	instance = get_object_or_404(Comments,id=id)
	instance.delete()
	return HttpResponse("ok")
