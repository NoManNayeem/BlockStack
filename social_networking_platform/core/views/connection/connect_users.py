from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from core.models.post import Post, PostSerializer
from core.models.connection import Connection, ConnectionSerializer

class ConnectionView(APIView):
    def post(self, request, format=None):
        connected_user_id = request.data.get('connected_user_id')
        user = request.user

        try:
            connected_user = User.objects.get(id=connected_user_id)
        except User.DoesNotExist:
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

        connection = Connection(user=user, connected_user=connected_user)
        connection.save()

        serializer = ConnectionSerializer(connection)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FeedView(APIView):
    def get(self, request, format=None):
        user = request.user

        connected_users = user.connections.filter(is_blocked=False).values_list('connected_user_id', flat=True)
        posts = Post.objects.filter(user__in=connected_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
