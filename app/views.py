from django.shortcuts import render, redirect
from django.urls import reverse
# internals
from .models import Post
# Create your views here.


def index(request):
    context = {
        "message":"Welcome to Django Deployment Digital Ocean Course",
        "posts" : Post.objects.all().order_by("-created_date")
    }
    if request.method == "POST":
        text = request.POST.get("text")
        image_url = request.POST.get("image_url")
        new_post = Post.objects.create(text=text, image_url=image_url)
        return redirect(reverse("app-index"))

    return render(request,"app/index.html",context=context)


def post_delete(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if post:
        post.delete()
        return redirect(reverse("app-index"))