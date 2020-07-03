from django.shortcuts import render
from django.http import HttpResponse
from .models import Post





def blog_home(request):
	context = {
	
	'posts' : Post.objects.all()
}
	return render(request, 'myBlog/blog_home.html', context )

def about(request):
	return render(request, 'myBlog/about.html', {'title': 'about'})
