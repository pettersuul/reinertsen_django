from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'domain': request.get_host(),
        'pages': client.entries({'content_type': 'page', 'order': 'fields.order', 'limit': 3}),
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
        'listings': client.entries({'content_type': 'page', 'fields.slug': 'work-listings'})[0],
        'contact':  client.entries({'content_type': 'contact'})[0],
        'footer':  client.entries({'content_type': 'footer'})[0]
    })

def references(request):
    return render(request, 'references.html', {
        'page': client.entries({'content_type': 'page', 'fields.slug': 'references'})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
        'footer':  client.entries({'content_type': 'footer'})[0]
        })

def reference_single(request, slug):
    try:
        reference = client.entries({'content_type': 'reference', 'fields.slug': slug})[0]
        return render(request, 'reference_single.html', {
            'reference': reference,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
            'footer':  client.entries({'content_type': 'footer'})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def listings(request):
    return render(request, 'work.html', {
        'page': client.entries({'content_type': 'page', 'fields.slug': 'work-listings'})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
        'footer':  client.entries({'content_type': 'footer'})[0]
        })

def listings_single(request, slug):
    try:
        listing = client.entries({'content_type': 'listing', 'fields.slug': slug})[0]
        return render(request, 'work-single.html', {
            'listing': listing,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
            'footer':  client.entries({'content_type': 'footer'})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def page(request, slug):
    try:
        page = client.entries({'content_type': 'page', 'fields.slug': slug})[0]
        return render(request, 'page.html', {
            'page': page,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order'}),
            'footer':  client.entries({'content_type': 'footer'})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))
