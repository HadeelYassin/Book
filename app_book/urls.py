from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('addbook', views.addbook),
    path('authors', views.index1),
    path('addauthor', views.addauthor),
    path('bookinfo/<num>', views.showb),
    path('process/<num>',views.addauthortobook),
]