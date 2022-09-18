from django.shortcuts import render
from diary.models import Page

def page_list(request):
    context = dict()
    object_list = Page.objects.all()
    context["object_list"] = object_list
    return render(request, 'diary/page_list.html', context)
