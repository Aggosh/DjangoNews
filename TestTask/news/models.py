from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField()
    author = models.ForeignKey(Author, related_name="post", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Author, related_name="comment", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
