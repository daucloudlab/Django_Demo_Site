from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comments
# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)

def template_two(request):
    t = get_template('myview.html')
    c = Context({'name':"Template Two"})
    return HttpResponse(t.render(c))

def template_three(request):
    return render(request, 'myview.html', {'name': 'Template Three'})

def articles(request):
    return render(request, 'articles.html', {'articles':Article.objects.all()})

def article(request, article_id):
    return render(request, 'article.html',
                  {'article':Article.objects.get(pk=article_id),
                   'comments':Comments.objects.filter(comments_article_id = article_id)})

