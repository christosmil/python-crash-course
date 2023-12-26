"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    # Page for adding a new post.
    path('new-post/', views.new_post, name='new-post'),
    # Page for editing an existing post.
    path('edit-post/<int:blog_post_id>', views.edit_post, name='edit-post'),
]