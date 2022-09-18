from django.shortcuts import render
from diary.models import Page

def page_list(request):
    context = dict()
    object_list = Page.objects.all()
    context["object_list"] = object_list
    return render(request, 'diary/page_list.html', context)


def page_detail(request, page_id):
    context = dict()
    object = Page.objects.get(id=page_id)
    context["object"] = object
    return render(request, 'diary/page_detail.html', context)
