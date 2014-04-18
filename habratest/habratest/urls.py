from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from vote.views import VoteListView, addvote
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'habratest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', VoteListView.as_view(), name="index"), 
    url(r'^plus/(?P<pk>\d+)/$', addvote, name='addvote'),
)
