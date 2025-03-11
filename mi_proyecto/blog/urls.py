from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='lista_posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detalle_post'),
    path('post/nuevo/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('api/posts/', views.PostAPI.as_view(), name='post_api'),
]