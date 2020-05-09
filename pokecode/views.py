from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.all() #crée l'objet liste de posts à partir du modèle Post
	return render(request,'blog/post_list.html', {'posts':posts}) #passe posts en argument au template
