from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.all() #crée l'objet liste de posts à partir du modèle Post
	return render(request,'blog/post_list.html', {'posts':posts}) #passe posts en argument au template


def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})