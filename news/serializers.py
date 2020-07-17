from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """
    Post model serializer
    """

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_id",
        )


class CommentSerializer(serializers.ModelSerializer):
    """
    Comment model serializer
    """

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "content", "creation_date")
