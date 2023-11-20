from django.shortcuts import render, redirect

from phones.models import Phone
def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    print(all_phones)
    sort = request.GET.get('sort', '')
    # print(sort_in)

    if sort == 'min_price':
        sort = 'price'
    elif sort == 'max_price':
        sort = '-price'
    else:
        sort = 'name'
    phones = all_phones.order_by(sort)
    context = {'phones':  phones}
    return render(request, template, context)



def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
