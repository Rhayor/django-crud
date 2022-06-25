from django.shortcuts import render
from django.views import DetailView, UpdateView

from ogundanamotunrayo.blog.models import Post

# Create your views here.

class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model = Post
    fields =" __all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields =" __all__"
    success_url = reverse_lazy("blog:all")



