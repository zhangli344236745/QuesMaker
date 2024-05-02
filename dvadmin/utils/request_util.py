from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.urls.resolvers import ResolverMatch

def get_request_user(request):
    user:AbstractBaseUser = getattr(request,'user',None)
    if user and user.is_authenticated():
        return user
    # try:
    #     user, tokrn = JWTAuthentication().authenticate(request)
    # except Exception as e:
    #     pass
    return user or AnonymousUser()
