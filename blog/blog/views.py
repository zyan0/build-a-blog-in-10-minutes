from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.blog.models import Article

def home(request):
	entries = Article.objects.all()
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))