from django.conf.urls import url
#from django.contrib import admin
from frontend import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^(?P<slug>[-\w]+)$', views.page)
]
