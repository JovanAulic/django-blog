from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

#def home(request):
#	return render(request, 'home.html', {})

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']


    
def CategoryView(request,cats):
	category_post = Post.objects.filter(kategorija=cats)
	return render(request, 'kategorije.html', {'cats': cats.title(), 'category_post': category_post})


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete-post.html'
	success_url = reverse_lazy('home')
	
		
	