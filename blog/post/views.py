from django.shortcuts import render
from .models import posts

def index(request):
    if request.method =='POST':
        titleblog = request.POST.get('title')
        bodyblog= request.POST.get('body')

        create_blog = posts.objects.create(title=titleblog,body=bodyblog)
        create_blog.save()
        get_post=posts.objects.filter()
        return render(request,'index.html',{'posts':get_post})
    return render(request,'index.html')

def b_posts(request):
    
    blog_post=posts.objects.get()
    return render(request,'posts.html',{'post':blog_post})
    
# Create your views here.
