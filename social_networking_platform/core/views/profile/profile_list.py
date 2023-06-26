from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.models.profile import Profile, ProfileSerializer


class ProfileView(generics.ListAPIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        return Profile.objects.all()