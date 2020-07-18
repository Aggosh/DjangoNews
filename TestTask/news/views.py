from rest_framework.generics import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from .models import Post, Author, Comment
from .serializers import PostSerializer, CommentSerializer


# Post
class PostView(ListCreateAPIView):
    """
    CRUD Post view
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get("author_id"))
        return serializer.save(author=author)


class SinglePostView(RetrieveUpdateDestroyAPIView):
    """
    CRUD view for single post
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpVotePost(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, pk):
        """
        view for up vote
        request post_id
        """
        instance = Post.objects.get(pk=pk)
        instance.amount_of_upvotes += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# Comment
class CommentView(ListCreateAPIView):
    """
    CRUD Comment view
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get("author_id"))
        post = get_object_or_404(Post, id=self.request.data.get("post_id"))
        return serializer.save(author=author, post=post)


class SingleCommentView(RetrieveUpdateDestroyAPIView):
    """
    CRUD view for single comment
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
