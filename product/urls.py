from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('product/<int:product_id>', views.detail, name='detail'),
    path('product/<int:product_id>/upvote', views.upvote, name='upvote'),
]