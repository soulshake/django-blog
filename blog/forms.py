from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta: #indique le modèle sur lequel se base le form
		model = Post
		fields = ('title', 'text',)
	