from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Category
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


class HomeView(View):
    def get(self, request):
        articles = Article.objects.all()
        main_news = articles[:7]
        featured_news = articles.order_by("?")[:10]
        latest_news = articles.order_by("-id")[:12]
        
        context = {
            "main_news": main_news,
            "featured_news": featured_news,
            "latest_news": latest_news
        }
        
        return render(request, 'index.html', context)


class ArticleDetailView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        article.views += 1
        article.save()
        
        similiar_news = Article.objects.filter(category=article.category).exclude(id=id).order_by("?")[:4]
        context = {
            "article": article,
            "similiar_news":similiar_news
        }
        return render(request, 'single.html', context)
            
            
            
            

class ContactView(View):
    form_class = ContactForm
    def get(self, request):
        return render(request, 'contact.html')
    
    def post(self, request):
        data = request.POST
        form = self.form_class(data=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz yuborildi")
            return redirect("contact")
            
        messages.error(request, "Nimadir xato ketdi")
        return render(request, 'contact.html')
        
        
class CategoryArticlesListView(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        articles = category.articles.all().filter(is_active=True)
        
        context = {
            'articles': articles
        }
        return render(request, 'category.html', context)
    
from django.utils import translation
from django.conf import settings

def language_switcher(request, lan):
    return redirect(f'/{lan}/')