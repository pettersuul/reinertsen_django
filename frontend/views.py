from django.http import Http404
from django.shortcuts import render
from .models import client

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'pages': client.entries(
            {'content_type': 'page', 'include': 3}
        )
    })

def page(request, slug):
    try:
        page = client.entries(
            {'content_type': 'page', 'fields.slug': slug, 'include': 3}
        )[0]
        return render(request, 'page.html', {'page': page})
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))
