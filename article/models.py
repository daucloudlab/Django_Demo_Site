# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length = 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default = 0)

    class Meta:
        db_table = "article"

    def __str__(self):
        return self.article_title



class Comments(models.Model):
    comments_text = models.TextField(verbose_name = "Коменттің мәтіні")
    comments_article = models.ForeignKey(Article)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comments_text

