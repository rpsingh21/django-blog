from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import Posts
from .forms import PostForms

# Create your views here.

def post_list(request):
	posts = Posts.objects.all()
	context ={
		'title':'Post-List',
		'posts':posts,
	}
	return render(request,"home.html",context)

def post_detail(request,slug):
	post = get_object_or_404(Posts,slug=slug)
	context={
		'title':post.title,
		'post':post
	}
	return render(request,"post-detail.html",context)

def post_create(request):
	form = PostForms(request.POST or None ,request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	context={
		'title':'Create New Post',
		'form':form,
	}
	return render(request,"blog-create-update.html",context)

def post_update(request,slug):
	instance = get_object_or_404(Posts,slug=slug)
	form = PostForms(request.POST or None, request.FILES or None,instance=instance)
	if request.method =='POST':
		if form.is_valid():
			instance=form.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	context={
		'tile':'update'+instance.title,
		'form':form,
	}
	return render(request,'blog-create-update.html',context)

def post_delete(request,slug):
	instance = get_object_or_404(Posts,slug=slug)
	instance.delete()
	return redirect('posts:list')