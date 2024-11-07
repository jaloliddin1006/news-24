from django.urls import path
from .views import HomeView, ArticleDetailView, ContactView, CategoryArticlesListView, language_switcher

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path("article/<int:id>/", ArticleDetailView.as_view(), name="detail"),
    path("contact", ContactView.as_view(), name="contact"),
    path("category/<int:id>", CategoryArticlesListView.as_view(), name="category_articles"),
    path("language/<str:lan>", language_switcher, name="language_switcher"),
]
