from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [

			{
				'author': 'Neeraj',
				'date_posted' : 'november, 24',
				'title' : 'Django is great',
				'content': "this is my post 1"
			},

			{
				'author': 'Akshay',
				'date_posted' : 'August, 09',
				'title' : 'Django is really great',
				'content': "this is my post 2"

			}
		]





def blog_home(request):
	context = {
	
	'posts' : Post.objects.all()
}
	return render(request, 'myBlog/blog_home.html', context )

def about(request):
	return render(request, 'myBlog/about.html', {'title': 'about'})
