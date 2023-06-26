from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from core.models.connection import Connection, ConnectionSerializer




class UserConnectionListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        connections = Connection.objects.filter(user=user)
        serializer = ConnectionSerializer(connections, many=True)
        return Response(serializer.data)



class ConnectionCreateView(APIView):
    permission_classes = [IsAuthenticated]
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

class ConnectionDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        user = request.user

        try:
            connection = Connection.objects.get(user=user, pk=pk)
        except Connection.DoesNotExist:
            return Response({'error': 'Connection not found'}, status=status.HTTP_404_NOT_FOUND)

        connection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
