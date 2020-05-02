from django.shortcuts import render, get_object_or_404
from .models import MyBlog

# Create your views here.
def blog_home(request):
	blogs = MyBlog.objects.order_by('-date')
	return render(request, 'blog/blog_home.html', {'blogs':blogs})

def detail(request, blog_id):
	blog =  get_object_or_404(MyBlog, pk=blog_id)
	return render(request, 'blog/detail.html', {'blog':blog})
