from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productview(request, myid):
    # Fetch the product using the id.
    prod = Product.objects.filter(id=myid)
    print(prod)
    return render(request, "shop/prodview.html", {"product": prod[0]})


def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get("itemsJson", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "") + request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        order = Order(
            items_json=itemsJson, 
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
        )
        order.save()
        return render(request, "shop/checkout.html", {"thank": 1, "id": order.order_id})
    return render(request, "shop/checkout.html")
