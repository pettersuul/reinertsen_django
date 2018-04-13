from django.conf.urls import url
#from django.contrib import admin
from frontend import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.posts),
    url(r'^posts/(?P<slug>[-\w]+)$', views.post_by_slug)
]
