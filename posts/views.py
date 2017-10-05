from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from .models import Posts, Tags
from comments.models import Comments
from .forms import PostForms
from comments.forms import CommentForm

# Create your views here.

def post_list(request):
	posts = Posts.objects.all()
	tags  = Tags.objects.all()
	tag   = request.GET.get('tag')
	if tag:
		print(tag)
		posts  = posts.filter(tags__name=tag)

	#  Now get Post data
	search = request.GET.get("search")
	if search:
		posts=posts.filter(
				Q(title__icontains=search)|
				Q(content__icontains=search)|
				Q(user__first_name__icontains=search) |
				Q(user__last_name__icontains=search)
				).distinct()

	# Paginator code
	page = request.GET.get('page', 1)
	paginator = Paginator(posts,2)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context ={
		'title':'Post-List',
		'posts':posts,
		'tags':tags,
	}
	return render(request,"home.html",context)

def post_detail(request,slug):
	post = get_object_or_404(Posts,slug=slug)
	Posts.objects.filter(slug=slug).update(views=(post.views+1))
	content_type = ContentType.objects.filter(model='posts').first()
	tags = Tags.objects.all()
	comments_count = Comments.objects.get_all().filter(object_id=post.id,content_type=content_type).count()
	context={
		'title':post.title,
		'post':post,
		'comments_count':comments_count,
		'tags':tags,
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