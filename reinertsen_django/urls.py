from django.conf.urls import url
#from django.contrib import admin
from frontend import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    url(r'^references/(?P<slug>[-\w]+)$', views.reference_single),
    url(r'^references', views.references),

    url(r'^work-listings/(?P<slug>[-\w]+)$', views.listings_single),
    url(r'^work-listings', views.listings),
    
    url(r'^(?P<slug>[-\w]+)$', views.page)
]
