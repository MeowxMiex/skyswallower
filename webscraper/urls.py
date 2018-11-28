from django.urls import path
from . import views

app_name = 'webscraper'
urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:author_id>/', views.detail, name='detail'),
    path('scrapesite/<int:website_id>/', views.scrapesite_detail, name='scrapesite_detail'),
    path('<int:author_id>/update', views.update, name='update')
]
