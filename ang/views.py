import os

from django.conf import settings
from django.http import HttpResponse, Http404

from django.views.generic import View

from django.shortcuts import render


class AngularTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        print(item)
        template_dir_path = settings.TEMPLATES[0]["DIRS"][0]
        final_path = os.path.join(template_dir_path, item + ".html")
        print(final_path)
        try:
            html = open(final_path)
            return HttpResponse(html)
        except:
            raise Http404
