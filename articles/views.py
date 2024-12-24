from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles


def home(request):
    articles = Articles.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)


def article_list(request):
    articles = Articles.objects.all()
    ctx = {'articles ': articles }
    return render(request, 'articles/students-list.html', ctx)


def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        if title and category and short_content and long_content and author:
            Articles.objects.create(
                title=title,
                category=category,
                short_content=short_content,
                long_content=long_content,
                author=author,
            )
            return redirect('home')
    return render(request, 'articles/add-post.html')


def article_detail(request, post_id):
    articles = get_object_or_404(Articles, pk=post_id)
    ctx = {'articles': articles}
    return render(request, 'articles/detail.html', ctx)

def article_by_category(request, category):
    articles = Articles.objects.filter(category=category)
    ctx = {'articles': articles, 'category': category}
    return render(request, 'articles/category.html', ctx)
