from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from core.models.post import Post, PostSerializer

class PostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        keyword = request.GET.get('')
        queryset = Post.objects.all()

        if keyword:
            queryset = queryset.filter(title__icontains=keyword)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
