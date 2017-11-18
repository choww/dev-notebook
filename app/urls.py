from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users import views as user_views
from notebook import views as notebook_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^login', user_views.signin, name='login'),   
    url(r'^signup', user_views.signup, name='signup'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^account', user_views.account, name='account'),
    url(r'^posts', notebook_views.index, name='all-posts'),
    url(r'^new-post', notebook_views.create, name='new-post'),
    url(r'^edit-post/(?P<id>\d+)/$', notebook_views.edit, name='edit-post')
]   
