from django.conf import settings
from django.urls import re_path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users import views as user_views
from notebook import views as notebook_views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    re_path(r'^login', user_views.signin, name='login'),
    re_path(r'^signup', user_views.signup, name='signup'),
    re_path(r'^logout', auth_views.LogoutView, {'next_page': '/'}, name='logout'),

    re_path(r'^dashboard', user_views.dashboard, name='dashboard'),
    re_path(r'^account/edit', user_views.edit, name='edit-account'),
    re_path(r'^account', user_views.show, name='account'),
    re_path(r'^posts/new', notebook_views.create, name='new-post'),
    re_path(r'^edit-post/(?P<id>\d+)/$', notebook_views.edit, name='edit-post'),
    re_path(r'^posts/delete/(?P<id>\d+)/$', notebook_views.destroy, name='delete-post'),
    re_path(r'^(?P<username>\w+)/$', notebook_views.index, name='all-posts'),
    re_path(r'^(?P<username>\w+)/tags/(?P<name>.+?)/$', notebook_views.tag, name='tag'),

    re_path(r'^forgot-password/done', auth_views.PasswordResetDoneView),
    re_path(r'^forgot-password', auth_views.PasswordResetView, {'success_url': '/forgot-password/done'}, name="forgot-pw"),
    re_path(r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView,
        {'post_reset_login' : False},
        name="pw-reset-confirm")
]
