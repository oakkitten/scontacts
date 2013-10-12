from registration.views import RegistrationView
from django.contrib.auth.models import User

class CustomRegView(RegistrationView):
    success_url = "/contacts/" 

    def register(self, request, **kwargs):
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password1']
	User.objects.create_user(username, email, password)
	
