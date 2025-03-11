from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'fecha_publicacion', 'autor']
        read_only_fields = ['fecha_publicacion', 'autor']  # Solo lectura para estos campos