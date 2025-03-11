from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# Vista para la página de índice (pública)
def index(request):
    return render(request, 'blog/index.html', {'titulo': 'Bienvenido al Blog'})

# Lista de posts (requiere login)
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']

# Detalle de un post (requiere login)
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'
    context_object_name = 'post'

# Crear un nuevo post (requiere login)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Actualizar un post existente (requiere login)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('lista_posts')

# Eliminar un post (requiere login)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('lista_posts')

# Vista para registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/registro.html', {'form': form})

# API para posts
class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(autor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)