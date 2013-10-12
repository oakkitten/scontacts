from django.conf.urls import patterns, url, include
from register.views import *
from register.forms import *
urlpatterns = patterns('',
	url(r'^register/$', CustomRegView.as_view(form_class=CustomForm), name='registration_register'),
	url(r'', include('registration.urls')),
)
