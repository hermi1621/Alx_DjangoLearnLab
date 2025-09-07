from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if not post:
        return Response({"detail": "Post not found."}, status=404)

    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({"detail": "You have already liked this post."}, status=400)

    Like.objects.create(user=request.user, post=post)

    # Notification
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id
        )

    return Response({"detail": "Post liked successfully."}, status=201)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if not post:
        return Response({"detail": "Post not found."}, status=404)

    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        return Response({"detail": "You have not liked this post."}, status=400)

    like.delete()
    return Response({"detail": "Post unliked successfully."}, status=204)
