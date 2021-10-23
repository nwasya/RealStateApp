from django.shortcuts import render

# Create your views here.
from RE_property.models import Property, PropertyImage


def search_for_property(request, *args, **kwargs):
    if request.method == 'POST':
        price = request.POST.get('price')
        size = request.POST.get('size')
        filters = {
            "city": request.POST.get('city'),
            "area": request.POST.get('area'),
            "status": request.POST.get('status'),
            "house_type": request.POST.get('type'),
            "bedroom": request.POST.get('bedroom'),
            "garage": request.POST.get('garage'),
            "size_start": get_range(size)[0],
            "size_end": get_range(size)[1],
            "price_start": get_range(price)[0],
            "price_end": get_range(price)[1],
        "type":"villa"}

        final_items = Property.objects.search_property(filters)
        context = {
            'items' : final_items
        }

    return render(request, 'property_items.html', context=context)




def get_property_detail(request,*args,**kwargs):
    print(kwargs['property_id'],'jjj')
    context = {}
    li = []
    obj = Property.objects.get(id=kwargs['property_id'])
    all_images = PropertyImage.objects.filter(Property_id=obj.id)
    for item in all_images:
        li.append(item)
    grouped_images = property_grouper(li)
    context['images'] = grouped_images
    context['property'] = obj
    print(context['images'])



    return render(request,'property_detail.html',context)

def get_range(str_range: str) -> list:
    b = []
    a = str_range.split()
    b.append(int(a[1]))
    b.append(int(a[3]))
    return b

def property_grouper(images : list)->dict:
    li = []
    dic = {}
    counter = 0
    for img in images:
        li.append(img)
        if len(li) == 5:
            dic[counter] = li
            li = []
            counter +=1
    dic[counter] = li
    return dic
