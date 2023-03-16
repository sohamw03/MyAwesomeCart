from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
import datetime

# Create your views here.
def index(request):
    blogpost = Blogpost.objects.values(
        "title", "pub_date", "chead0", "thumbnail", "post_id"
    )
    return render(request, "blog/index.html", {"allPosts": blogpost})


def blogpost(request, post_id):
    blogpost = Blogpost.objects.filter(post_id=post_id)
    allpost = Blogpost.objects.values()
    lst = [int(i["post_id"]) for i in allpost]
    lst.sort()
    min_id, max_id = min(lst), max(lst)
    return render(
        request,
        "blog/blogpost.html",
        {"blogpost": blogpost, "min_id": min_id, "max_id": max_id},
    )
