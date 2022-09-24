from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.urls import reverse
from diary.models import Page
from .forms import PageForm


def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 8)
    curr_page_num = request.GET.get('page')
    if curr_page_num == None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    return render(request, 'diary/page_list.html', {'page': page})


def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object': object})


def info(request):
    return render(request, 'diary/info.html')


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})


def page_update(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=object) 
        # instance로 기존에 존재하는 데이터를 재사용 
        # instance가 없으면 새로운 포스트가 만들어짐
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=object.id)
    else:
        form = PageForm(instance=object) # instance로 기존에 존재하는 데이터를 사용한다.
    return render(request, 'diary/page_form.html', {'form': form})


def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm_delete.html', {'object': object})


def index(request):
    return render(request, 'diary/index.html')

