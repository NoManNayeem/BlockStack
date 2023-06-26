from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    text = models.TextField()
    image = models.ImageField(upload_to='post_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
