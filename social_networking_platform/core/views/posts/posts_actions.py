from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import AllowAny,IsAuthenticated

from core.models.post import Post, PostSerializer 
from core.models.like import Like, LikeSerializer
from core.models.comment import Comment, CommentSerializer
from core.models.share import Share, ShareSerializer

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostLikeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)

        new_like = Like(user=user, post=post)
        new_like.save()
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)

class PostCommentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        user = request.user

        comment_text = request.data.get('comment', '')

        new_comment = Comment(user=user, post=post, text=comment_text)
        new_comment.save()

        serializer = CommentSerializer(new_comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostShareView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        user = request.user

        new_share = Share(user=user, post=post)
        new_share.save()

        serializer = ShareSerializer(new_share)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
