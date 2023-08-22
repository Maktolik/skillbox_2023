from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=False, blank=True)

    def __str__(self):
        return f"{self.name!r}"


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name!r}"


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name!r}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return f"{self.title!r}"

    def get_absolute_url(self):
        return reverse("blogapp:article_detail", kwargs={"pk": self.pk})