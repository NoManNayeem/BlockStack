from django.db import models
from django.contrib.auth.models import User
from .post import Post
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.post}"

from rest_framework import serializers

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'
