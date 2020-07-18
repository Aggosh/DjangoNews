from django.urls import path
from .views import PostView, SinglePostView, UpVotePost
from .views import CommentView, SingleCommentView

app_name = "Post"

urlpatterns = [
    path("post/", PostView.as_view()),
    path("post/<int:pk>", SinglePostView.as_view()),
    path("postupvote/<int:pk>", UpVotePost.as_view()),
    path("comment/", CommentView.as_view()),
    path("comment/<int:pk>", SingleCommentView.as_view()),
]
