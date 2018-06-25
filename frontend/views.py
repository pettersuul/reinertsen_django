from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

def checklocale(domain):
    eng = '.com'
    no  = '.no'

    if domain.endswith(no):
        return 'nb-NO'
    else:
        return 'en-US'

# Create your views here.

def index(request):
    locale = checklocale(request.get_host()),
    return render(request, 'index.html', {
        'locale': locale,
        'pages': client.entries({'content_type': 'page', 'order': 'fields.order', 'limit': 3, 'locale': locale}),
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
        'listings': client.entries({'content_type': 'page', 'fields.slug': 'work-listings', 'locale': locale})[0],
        'contact':  client.entries({'content_type': 'contact', 'locale': locale})[0],
        'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
    })

def references(request):
    locale = checklocale(request.get_host()),
    return render(request, 'references.html', {
        'page': client.entries({'content_type': 'page', 'fields.slug': 'references', 'locale': locale})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
        'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
        })

def reference_single(request, slug):
    try:
        locale = checklocale(request.get_host()),
        reference = client.entries({'content_type': 'reference', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'reference_single.html', {
            'reference': reference,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
            'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def listings(request):
    locale = checklocale(request.get_host()),
    return render(request, 'work.html', {
        'page': client.entries({'content_type': 'page', 'fields.slug': 'work-listings', 'locale': locale})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
        'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
        })

def listings_single(request, slug):
    try:
        locale = checklocale(request.get_host()),
        listing = client.entries({'content_type': 'listing', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'work-single.html', {
            'listing': listing,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
            'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def page(request, slug):
    try:
        locale = checklocale(request.get_host()),
        page = client.entries({'content_type': 'page', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'page.html', {
            'page': page,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
            'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))
