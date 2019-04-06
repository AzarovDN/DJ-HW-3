from django.shortcuts import render
from phones.models import Phone
# from operator import itemgetter

# sortedlist = sorted(alist, key=lambda x: (x.firstname , x.lastname))

def show_start(request):
    return render(
        request,
        'index.html'
    )


def show_catalog(request):
    phone_list = list(Phone.objects.all())
    sort = request.GET.get('sort')
    name = ''
    min_price = ''
    max_price = ''

    if sort == 'name':
        name = 'disabled'
        phone_list = sorted(phone_list, key=lambda x: x.name)

    if sort == 'min_price':
        min_price = 'disabled'
        phone_list = sorted(phone_list, key=lambda x: x.price)

    if sort == 'max_price':
        max_price = 'disabled'
        phone_list = sorted(phone_list, key=lambda x: x.price, reverse=True)

    return render(
        request,
        'catalog.html', {'phone_list': phone_list,
                         'name': name,
                         'min_price':  min_price,
                         'max_price': max_price
                         }
    )


def show_product(request, slug):
    phone_list = list(Phone.objects.all())
    for phone in phone_list:
        if phone.slug == slug:

            return render(
                request,
                'product.html', {'phone': phone}
            )
