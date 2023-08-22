from django.contrib.gis.feeds import Feed
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse

from blogapp.models import Article


class ArticlesListView(ListView):
    queryset = (
        Article.objects
        .select_related("author", "category")
        .prefetch_related("tags")
        .defer("content")
    )

class ArticleDetailView(DetailView):
    model = Article
    template_name = "blogapp/article_detail.html"


class LatestArticlesFeed(Feed):
    title = "Last articles"
    description = "Updates"
    link = reverse_lazy("blogapp:articles_list")

    def items(self):
        return (
        Article.objects
        .select_related("author", "category")
        .prefetch_related("tags")
        .defer("content")[:2]
    )

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.content[:50]

