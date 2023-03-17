from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
import datetime

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


def searchMatch(query, item):
    if (
        (query in item.product_name.lower())
        or (query in item.category.lower())
        or (query in item.subcategory.lower())
        or (query in item.desc.lower())
    ):
        return True
    else:
        return False


def search(request):
    query = request.GET.get("search").lower()
    allProds = []
    catprods = Product.objects.values("category", "id")
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds": allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {"msg": "Please make sure to enter relevant search query"}
    print(len(allProds))
    return render(request, "shop/search.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, "shop/contact.html", {"thank": thank})


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id", "")
        email = request.POST.get("email", "")
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append(
                        {
                            "text": item.update_desc,
                            "time": item.timestamp.strftime("%d-%m-%Y"),
                        }
                    )
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            print(str(e))
            return HttpResponse("{}")
    return render(request, "shop/tracker.html")


def productview(request, myid):
    # Fetch the product using the id.
    prod = Product.objects.filter(id=myid)
    return render(request, "shop/prodview.html", {"product": prod[0]})


def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get("itemsJson", "")
        amount = request.POST.get("amount", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address", "") + request.POST.get("address2", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        order = Order(
            items_json=itemsJson,
            amount=amount,
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
        )
        order.save()
        update = OrderUpdate(
            order_id=order.order_id, update_desc="The order has been placed."
        )
        update.save()
        return render(request, "shop/checkout.html", {"thank": 1, "id": order.order_id})
    return render(request, "shop/checkout.html")
