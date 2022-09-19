from django.shortcuts import render, redirect
from diary.models import Page
from .forms import PageForm

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


def info(request):
    return render(request, 'diary/info.html')


def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        new_page = form.save()
        return redirect('page-detail', page_id=new_page.id)
    else:
        context = dict()
        form = PageForm()
        context["form"] = form
        return render(request, 'diary/page_form.html', context)
    
