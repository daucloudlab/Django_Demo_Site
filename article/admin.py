from django.contrib import admin
from models import Article, Comments

# Register your models here.

class ArticleInline(admin.TabularInline):
    model = Comments
    extra = 3


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInline]

admin.site.register(Article, ArticleAdmin)
