# from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from core.models.user_serializer import UserSerializer
from core.models.profile import Profile, ProfileSerializer

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny,]
    def post(self, request):
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        # email = request.POST.get("email",None)
        if username and password:
            # Create a new user with hashed password
            new_user = User.objects.create_user(username=username, password=password)
            # Save the user object
            new_user.save()
            return Response({"message":"Created New User!"}, status=status.HTTP_400_BAD_REQUEST)



        return Response({"message":"Failed to create new user!"}, status=status.HTTP_400_BAD_REQUEST)
