from django.conf.urls import patterns, include, url
from  blogsite import views, feeds, forms

urlpatterns = patterns('',
              url(r'^$', views.Archive.as_view(), name='archive'),
              url(r'^(?P<post_id>\d+)$', views.process_comment, name='comment'),
              url(r'^(?P<pk>\d+)/$', views.Post.as_view(), name='post'),
              url(r'^feeds/$', feeds.LatestEntriesFeed()),
              url(r'^excel$', views.to_excel),
              )