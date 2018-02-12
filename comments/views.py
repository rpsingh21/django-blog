from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType

from .models import Comments
from .forms import CommentForm
from activitys.models import Activitys

# Create your views here.


def instance_comments(request, object_id, slug):
    content_type = ContentType.objects.filter(model='posts').first()
    comments = Comments.objects.all().filter(object_id=object_id, content_type=content_type).distinct().order_by('timestamp')
    initial_data = {
        "content_type": content_type,
        "slug": slug
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    context = {
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'comments/comments.html', context)


def reply_form(request, slug, parent_id):
    initial_data = {
        "content_type": "posts",
        "slug": slug,
        "parent_id": parent_id,
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)

    context = {
        'comment_form': comment_form,
        "parent_id": parent_id,
    }
    return render(request, 'reply_form.html', context)


def comment_activity(request, id, activity_type):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)
    if not activity_type in ["F", "D", "U"]:
        return HttpResponse(status=404)

    data = 'DE'
    content_type = ContentType.objects.filter(model='comments').first()
    # . model_class()
    activity = Activitys.objects.filter(object_id=id, user=request.user, content_type=content_type)
    if activity_type == 'F':
        activity = activity.filter(activity_type='F')
        if activity.exists():
            activity.delete()
        else:
            Activitys.objects.create(
                    user=request.user,
                    activity_type=activity_type,
                    content_type=content_type,
                    object_id=id,
                    )
            data = activity_type
    else:
        activity = activity.filter(activity_type__in=['U', 'D'])
        if activity.exists():
            if activity.first().activity_type == activity_type:
                activity.delete()
            else:
                activity.update(activity_type=activity_type)
                data = activity_type
        else:
            Activitys.objects.create(
                user=request.user,
                activity_type=activity_type,
                content_type=content_type,
                object_id=id,
                )
            data = activity_type
    return HttpResponse(data)


def comment_delete(request, id):
    instance = get_object_or_404(Comments, id=id)
    instance.delete()
    return HttpResponse("ok")
