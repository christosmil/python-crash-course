from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm


def index(request):
    """The home page for Blog."""
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new-post.html', context)


@login_required
def edit_post(request, blog_post_id):
    """Edit an existing post."""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    check_post_owner(blog_post.owner, request.user)

    if request.method != 'POST':
        # Initial request; pre-fill with the current entry.
        form = PostForm(instance=blog_post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blog_post': blog_post, 'form': form}
    return render(request, 'blogs/edit-post.html', context)


def check_post_owner(post_owner, user):
    """Checks if the post owner is the current user."""
    if post_owner != user:
        raise Http404