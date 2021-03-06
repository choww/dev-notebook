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

    url(r'^dashboard', user_views.dashboard, name='dashboard'),
    url(r'^account/edit', user_views.edit, name='edit-account'),
    url(r'^account', user_views.show, name='account'),
    url(r'^posts/new', notebook_views.create, name='new-post'),
    url(r'^edit-post/(?P<id>\d+)/$', notebook_views.edit, name='edit-post'),
    url(r'^posts/delete/(?P<id>\d+)/$', notebook_views.destroy, name='delete-post'),
    url(r'^(?P<username>\w+)/$', notebook_views.index, name='all-posts'),
    url(r'^(?P<username>\w+)/tags/(?P<name>.+?)/$', notebook_views.tag, name='tag'),

    url(r'^forgot-password/done', auth_views.password_reset_done),
    url(r'^forgot-password', auth_views.password_reset, {'post_reset_redirect': '/forgot-password/done'}, name="forgot-pw"),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        auth_views.password_reset_confirm, 
        {'post_reset_redirect' : '/login'},
        name="pw-reset-confirm")
]   
