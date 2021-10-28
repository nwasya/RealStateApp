from django.http import Http404
from django.shortcuts import render, redirect

from RE_comment.models import PropertyComment
from RE_info.models import Info
from RE_news.models import News
from RE_property.models import Property, Type
from RE_user.models import SiteUser

categories = ['restaurant',
                  'house',
                  'garden',
                  'villa',
                  'apartment',
                  'store']

def home(request, *args, **kwargs):
    info = Info.objects.get()
    data = Property.objects.filter(is_slider=True)
    # info
    context = {'info': {'email': info.email,
                        'site_name': info.site_name,
                        'phone': info.phone,
                        'address': info.address},
                        'slider': data,

               }

    #############
    categories = Type.objects.all()

    for category in categories:

        x = Property.objects.filter(type__title__exact=category.title)
        count = x.count()
        y = x.order_by('-added_date')[:6]
        context[category.value] = y
        context[category.value + '_count'] = count
    x = Property.objects.all().order_by('-added_date')[:6]


    context['all'] = x
    featured = Property.objects.filter(is_featured=True)
    context['featured'] = featured
    ################################# News
    news = News.objects.all().order_by('-added_date')[:5]
    context['news'] = news
    ############################
    agents = SiteUser.objects.all().order_by('rate')[:3]
    context['agents'] = agents

    #################################
    comments = PropertyComment.objects.all()[:6]
    context['comments'] = comments


    return render(request, 'index.html', context)


def header(request, *args, **kwargs):
    info = Info.objects.get()

    context = {'email': info.email,
               'site_name': info.site_name,
               'phone': info.phone,
               'address': info.address
               }

    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {

    }
    return render(request, 'shared/Footer.html', context)


def get_latest_properties_by_category(request):
    context = {}
    categories = ['restaurant',
                  'house',
                  'garden',
                  'villa',
                  'apartment',
                  'store']
    for category in categories:
        x = Property.objects.filter(type__exact=category)
        items = x.order_by('-added_date')[:6]
        context[category] = items
    x = Property.objects.all().order_by('-added_date')[:6]
    context['all'] = x
    items = {
        'items': context
    }

    return render(request, 'index.html', items)
