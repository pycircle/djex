from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post-list/', 'blog.views.post_list', name="post_list"),
    url(r'^post/(?P<pk>\d+)/', 'blog.views.post_detail', name="post_detail"),
    url(r'^post/add/', 'blog.views.post_create', name="post_create"),
)
