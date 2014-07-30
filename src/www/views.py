from django.shortcuts import render, render_to_response, RequestContext
from www.models import Category, Post
from django.core.paginator import Paginator

def index(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 2)

	pag = request.GET.get('page')
	try:
		posts_list = paginator.page(pag)
	except:
		posts_list = paginator.page(1)

	categories = Category.objects.all()
	ctx = {}
	ctx['msg'] = 'My Blog'
	ctx['posts'] = posts_list
	ctx['all_posts'] = posts
	ctx['categories'] = categories
	return render_to_response('www/index.html', ctx, context_instance=RequestContext(request))


def post(request, slug_name):
	post_query = Post.objects.filter(slug=slug_name)
	post = post_query[0]
	posts_related = Post.objects.filter(category=post.category.id).exclude(id=post.id)
	ctx = {}
	ctx['post'] = post
	ctx['category'] = post.category
	ctx['related_posts'] = posts_related
	return render_to_response('www/post.html', ctx, context_instance=RequestContext(request))
