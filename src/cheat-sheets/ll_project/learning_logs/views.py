from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from .models import Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topic(request, topic_id):
    """Show a topic and all its entries."""
    topics = Topic.objects.filter(owner=request.user)
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries,
    }
    return render(request, 'learning_logs/topic.html', context)