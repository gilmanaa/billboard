from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from datetime import date

@login_required
def index(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,'SocialBoard/index.html',context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse("socialboard:index"))
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{"form":form})

@csrf_protect
def add_new_post(request):
    if request.method == "POST":
        new_post = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author'),
            'publish_date': date.today()
        }
        Post.objects.create(**new_post)
        return HttpResponse(status=201)
    else:
        return {"error": "didn't add post"}