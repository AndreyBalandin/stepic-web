from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^question/(?P<id>\d+)/', 'question', name='question'),
    url(r'^popular/', 'popular', name='popular'),
    url(r'^ask/', 'ask', name='ask'),
    url(r'^answer/', 'answer', name='answer'),
    url(r'^login/', 'my_login', name='login'),
    url(r'^signup/', 'signup', name='signup'),
    url(r'^$', 'main', name='main'),

    )
