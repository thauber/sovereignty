from django.conf.urls.defaults import *

urlpatterns = patterns('nationstates.views',
    url(
        r'^home/$',
        'home',
        name='sg_home'
    ),
    url(
        r'^enemies/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'relation_list',
        {'list_type': 'enemy'},
        name='sg_enemies'
    ),
    url(
        r'^allies/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'relation_list',
        {'list_type': 'ally'},
        name='sg_allies'
    ),
    url(
        r'^ally/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'relate',
        {'relation_type': 'ally'}
        name='sg_follow'
    ),
    url(
        r'^unally/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'unrelate',
        {'relation_type': 'ally'}
        name='sg_unfollow'
    ),
    url(
        r'^oppose/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'relate',
        {'relation_type': 'ally'}
        name='sg_follow'
    ),
    url(
        r'^unoppose/(?P<state_slug>[a-zA-Z0-9_-]+)/$',
        'unrelate',
        {'relation_type': 'ally'}
        name='sg_unfollow'
    ),