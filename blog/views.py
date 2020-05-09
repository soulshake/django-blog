from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# Create your views here.
def post_list(request,pageNb=1):
	posts = Post.objects.all().order_by('published_date') #crée l'objet liste de posts à partir du modèle Post
	pages = Paginator(posts,3)
	posts = pages.page(pageNb)
	previous = pageNb - 1
	next = pageNb + 1
	return render(request,'blog/post_list.html', {'posts':posts, 'pageNb':pageNb, 'previous': previous, 'next':next}) #passe posts en argument au template


def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if request.method == 'POST':
		form= PostForm(request.POST) #prend en photo ce qu'y a été envoyé et le met dans une variable
		if form.is_valid():
			post = form.save(commit=False) #immortalise la photo 
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
		return render(request,'blog/post_edit.html', {'form':form})