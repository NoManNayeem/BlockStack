from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework import permissions
from core.models.user_serializer import UserSerializer
from core.models.profile import Profile, ProfileSerializer

class CreateProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def post(self, request):
        try:
            profile_picture = request.FILES.get('profile_picture')
            user = request.user
            email = request.POST.get("email", None)
            bio = request.POST.get("bio", None)
            social_media_links = request.POST.get("social_media_links", None)

            if profile_picture and user and email and bio and social_media_links:
                # Find User
                new_user = user
                if not Profile.objects.filter(user=new_user).exists():
                    new_profile = Profile(user=new_user, bio=bio, profile_picture=profile_picture, social_media_links=social_media_links)
                    new_profile.save()
                    return Response({"message": "Created New Profile!"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "Profile Already Exists!"}, status=status.HTTP_409_CONFLICT)
            else:
                return Response({"message": "Missing required fields!"}, status=status.HTTP_400_BAD_REQUEST)
    
        except ValidationError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            return Response({"message": "An error occurred while creating the profile."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
