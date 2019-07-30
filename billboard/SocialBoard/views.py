from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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
            login(request, new_user)
            return HttpResponseRedirect(reverse("socialboard:index"))
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{"form":form})