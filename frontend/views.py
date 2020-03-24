from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import client

def checklocale(domain):
    eng = '.com'
    no  = '.no'

    if domain.endswith(eng):
        return 'en-US'
    else:
        return 'nb-NO'

# Create your views here.

def index(request):
    locale = checklocale(request.get_host()),
    return render(request, 'index.html', {
        'locale': locale,
        'page': client.entries({'content_type': 'page', 'fields.slug': 'index', 'locale': locale})[0],
        'nav': client.entries({'content_type': 'menu', 'locale': locale})
    })

def page(request, slug):
    try:
        locale = checklocale(request.get_host()),
        page = client.entries({'content_type': 'page', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'page.html', {
            'locale': locale,
            'page': page,
            'nav': client.entries({'content_type': 'menu', 'locale': locale})
            })
    except IndexError:
        raise Http404()

def references(request):
    locale = checklocale(request.get_host()),
    return render(request, 'references.html', {
        'locale': locale,
        'page': client.entries({'content_type': 'page', 'fields.slug': 'references', 'locale': locale})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
        'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
        })

def reference_single(request, slug):
    try:
        locale = checklocale(request.get_host()),
        reference = client.entries({'content_type': 'reference', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'reference_single.html', {
            'locale': locale,
            'reference': reference,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
            'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))

def listings(request):
    locale = checklocale(request.get_host()),
    return render(request, 'work.html', {
        'locale': locale,
        'page': client.entries({'content_type': 'page', 'fields.slug': 'work-listings', 'locale': locale})[0],
        'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
        'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
        })

def listings_single(request, slug):
    try:
        locale = checklocale(request.get_host()),
        listing = client.entries({'content_type': 'listing', 'fields.slug': slug, 'locale': locale})[0]
        return render(request, 'work-single.html', {
            'locale': locale,
            'listing': listing,
            'nav':  client.entries({'content_type': 'page', 'order': 'fields.order', 'locale': locale}),
            'footer':  client.entries({'content_type': 'footer', 'locale': locale})[0]
            })
    except IndexError:
        raise Http404('Post not found for slug: {0}'.format(slug))
