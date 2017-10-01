from django.shortcuts import render
from django.http import HttpResponse

from comments.models import  Comments

# Create your views here.

def instance_comments(request,object_id):
	comments = Comments.objects.all().filter(object_id=object_id).distinct().order_by('timestamp')
	context = {
		'comments':comments
	}
	return render(request,'comments.html',context)

	