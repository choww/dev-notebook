from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^account/', user_views.account, name='account'),
    url(r'^login/', user_views.signin, name='login'),   
    url(r'^signup/', user_views.signup, name='signup'),
    url(r'^logout/', auth_views.logout, name='logout')
]   
