from django.shortcuts import render, redirect
from blog import views

def index(request):
    if request.user.is_authenticated:
        return views.PostListView.as_view()(request)  # Usuario logueado: Lista de posts
    return redirect('login/')

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido']  # Especifica los campos del formulario
    template_name_suffix = '_create_form' # Sufijo para la plantilla de creación
    success_url = reverse_lazy('post_list')  # Redirige a la lista después de crear

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']  # Especifica los campos del formulario
    template_name_suffix = '_update_form' # Sufijo para la plantilla de actualización
    success_url = reverse_lazy('post_list')  # Redirige a la lista después de actualizar

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # Redirige a la lista después de borrar

from rest_framework import generics
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer