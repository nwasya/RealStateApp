from django.shortcuts import render

# Create your views here.
from RE_property.models import Property, PropertyImage, Type, Features, Status


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
            "type": "villa"}

        final_items = Property.objects.search_property(filters)
        context = {
            'items': final_items
        }

    return render(request, 'property_items.html', context=context)


def get_property_detail(request, *args, **kwargs):
    print(kwargs['property_id'], 'jjj')
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

    return render(request, 'property_detail.html', context)


def save_property(request):
    title = []
    if request.method == 'POST':
        title = request.POST['title']

        description = request.POST['content']
        short_description = request.POST['short_content']

        address = request.POST['Address']
        neighborhood = request.POST['neighborhood']
        city = request.POST['City']
        part = request.POST['part'] if 'part' in request.POST else None
        country = request.POST['Country']
        postal = request.POST['postal'] if "postal" in request.POST else None

        apartment = request.POST['apartment'] if 'apartment' in request.POST else None
        house = request.POST['house'] if 'house' in request.POST else None
        store = request.POST['store'] if 'store' in request.POST else None
        villa = request.POST['villa'] if 'villa' in request.POST else None
        garden = request.POST['garden'] if 'garden' in request.POST else None
        restaurant = request.POST['restaurant'] if 'restaurant' in request.POST else None
        li = [apartment, house, store, villa, garden, restaurant]
        type_li = distinct_none_values(li)

        exchange = request.POST['exchange'] if 'exchange' in request.POST else None
        sale = request.POST['sale'] if 'sale' in request.POST else None
        rent = request.POST['rent'] if 'rent' in request.POST else None
        li = [exchange, sale, rent]
        status_li = distinct_none_values(li)

        price = request.POST['price']
        sec_price = request.POST['sec_price'] if (
                    'sec_price' in request.POST and request.POST['sec_price'] != "") else 0
        monthly_price = request.POST['monthly_price'] if (
                    'monthly_price' in request.POST and request.POST['monthly_price'] != "") else 0

        cooling = request.POST['cooling'] if 'cooling' in request.POST else None
        heater = request.POST['heater'] if 'heater' in request.POST else None
        refrigerator = request.POST['refrigerator'] if 'refrigerator' in request.POST else None
        washer = request.POST['washer'] if 'washer' in request.POST else None
        barbeque = request.POST['barbeque'] if 'barbeque' in request.POST else None
        lawn = request.POST['lawn'] if 'lawn' in request.POST else None
        sauna = request.POST['sauna'] if 'sauna' in request.POST else None
        wifi = request.POST['wifi'] if 'wifi' in request.POST else None
        cabinet = request.POST['cabinet'] if 'cabinet' in request.POST else None
        microwave = request.POST['microwave'] if 'microwave' in request.POST else None
        pool = request.POST['pool'] if 'pool' in request.POST else None
        window = request.POST['window'] if 'window' in request.POST else None
        gym = request.POST['gym'] if 'gym' in request.POST else None
        phone = request.POST['phone'] if 'phone' in request.POST else None
        antenna = request.POST['antenna'] if 'antenna' in request.POST else None
        villa = request.POST['villa'] if 'villa' in request.POST else None
        li = [cooling,
              heater,
              refrigerator,
              washer,
              barbeque,
              lawn,
              sauna,
              wifi,
              cabinet,
              microwave,
              pool,
              window,
              gym,
              phone,
              antenna,
              villa]
        features_li = distinct_none_values(li)

        my_images = request.FILES.getlist('images[]')

        property_id = request.POST['code']
        area = request.POST['area']
        area_unit = request.POST['area_unit']
        bedroom = request.POST['bedroom']
        bathroom = request.POST['bathroom']
        garage = request.POST['garage']
        floor = request.POST['floor']
        garage_area = request.POST['garage_area']
        year = request.POST['year'] if 'year' in request.POST else None
        video_link = request.POST['video_link'] if 'video_link' in request.POST else None

        obj = Property(title=title,
                       description=description,
                       property_id=property_id,
                       user=request.user,
                       city=city,
                       part=part,
                       bedroom=bedroom,
                       bathroom=bathroom,
                       floor=floor,
                       area=area,
                       garage_area=garage_area,
                       area_unit=area_unit,
                       price=price,
                       sec_price=sec_price,
                       monthly_price=monthly_price,
                       address=address,
                       garage=garage,
                       short_description=short_description,
                       videos=video_link,
                       postal=postal,
                       country=country,
                       year=year)

        obj.save()

        for item in type_li:
            id = Type.objects.get(value__exact=item).id
            obj.type.add(id)
        for item in features_li:
            id = Features.objects.get(value__exact=item).id

            obj.features.add(id)
        for item in status_li:
            id = Status.objects.get(value__exact=item).id
            obj.status.add(id)

        for image in my_images:
            pi = PropertyImage(Property=obj, images=image)
            pi.save()

        obj.save()

    context = {}
    return render(request, 'add_property.html', context)


def get_range(str_range: str) -> list:
    b = []
    a = str_range.split()
    b.append(int(a[1]))
    b.append(int(a[3]))
    return b


def property_grouper(images: list) -> dict:
    li = []
    dic = {}
    counter = 0
    for img in images:
        li.append(img)
        if len(li) == 5:
            dic[counter] = li
            li = []
            counter += 1
    dic[counter] = li
    return dic


def distinct_none_values(li: list) -> list:
    ret = []
    for i in li:
        if i != None:
            ret.append(i)

    return ret
