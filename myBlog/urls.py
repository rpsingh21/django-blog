"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from ang.views import AngularTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('api/comments/', include(('comments.api.urls', 'comments'), namespace='comment-api')),
    path('api/activitys/', include(('activitys.api.urls', 'activitys'), namespace='activitys-api')),
    path('comments/', include(('comments.urls', 'comments'), namespace='comments')),
    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('markdownx/', include('markdownx.urls')),
    # path('api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$',  AngularTemplateView.as_view()),
    # path('api/posts/',include('posts.api.urls',namespace='posts-api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns +=  [
#   url(r'', TemplateView.as_view(template_name='base.html'))
# ]
