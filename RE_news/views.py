from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from RE_comment.models import NewsComment
from RE_news.models import News


def get_news(request, *args, **kwargs):
    context = {}

    news = News.objects.get(id=kwargs['id'])
    context['first_part_dec'] = news.description[:128]
    context['main_news'] = news

    #######
    other_news = News.objects.all().exclude(id=kwargs['id']).order_by('-added_date')

    context['other_news'] = other_news

    return render(request, 'blog.html', context=context)



def get_news_list(request):
    all_news = News.objects.all().order_by('-added_date')
    context = {'all_news':all_news}
    return render(request,'news_list.html',context)
# class GetNews(ListView):
#     template_name = 'blog.html'
#
#     paginate_by = 3
#
#     def get_queryset(self):
#         return News.objects.all()
#
#     def get_context_data(self, *args,**kwargs):
#         context = {}
#
#         news = self.object_list.get(id=kwargs['id'])
#         context['first_part_dec'] = news.description[:128]
#         context['main_news'] = news
#
#         #######
#         other_news = self.object_list.exclude(id=kwargs['id']).order_by('-added_date')[:3]
#
#         context['other_news'] = other_news
#         return context


def get_news_detail(request, *args, **kwargs):
    obj = News.objects.get(id=kwargs['id'])
    related = News.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        text = request.POST['text']
        print(full_name, email, text)
        product_object = News.objects.get(id=kwargs['id'])
        NewsComment.objects.create(full_name=full_name, email=email, text=text, object=product_object,
                                       confirmed=False).save()

        return HttpResponseRedirect(f'/blog-detail/{kwargs["id"]}')

    comment_list = NewsComment.objects.filter(object__id=kwargs['id'], confirmed=True).all()
    context = {
        'comments': comment_list,
        'new': obj,
        'related': related
    }
    return render(request, 'blog_detail.html', context=context)
