#-*-coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from article.models import Article, Comments
from django.core.urlresolvers import reverse
from forms import CommentForm
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

def article(request, article_id = 1):
    comment_form = CommentForm()
    args = {}
    args['article'] = Article.objects.get(pk = article_id)
    args['comments'] = Comments.objects.filter(comments_article_id = article_id)
    args['form'] = comment_form
    return render(request, 'article.html', args)

def addlike(request, article_id):
    try:
        article_object = Article.objects.get(pk = article_id)
        article_object.article_likes += 1
        article_object.save()
    except Article.DoesNotExist:
        raise Http404("Объект табылмады")
    return HttpResponseRedirect(reverse('article:all'))

def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.comments_article_id = article_id
            form.comments_article = Article.objects.get(pk = article_id)
            form.save()
    return HttpResponseRedirect(reverse('article:detail',args = (article_id,)))