from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.models.profile import ProfileSerializer

class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
