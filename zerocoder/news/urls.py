from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),
    path('create_news', views.create_news, name='add_news'),
    # path('page3', views.page3, name='page3'),
    # path('page4', views.page4, name='page4')
]
