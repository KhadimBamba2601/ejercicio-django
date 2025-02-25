from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # name corregido y sin duplicación
    path('posts/', views.PostListView.as_view(), name='post_list'), # Añadido 'posts/' para diferenciar del index
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/login.html'), name='logout'),
    path('api/post/', views.PostList.as_view(), name='post_list_api'),
    path('api/post/<int:pk>/', views.PostDetail.as_view(), name='post_detail_api'),
    path('api/post/create/', views.PostCreate.as_view(), name='post_create_api'),
    path('api/post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update_api'),
    path('api/post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete_api'),
]