from django.db import models
from django.contrib.auth.models import User


class Connection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    connected_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connected_users')
    is_blocked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user} => {self.connected_user}"


from rest_framework import serializers

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'
