from urllib import request
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
        return False
    return user_passes_test(in_groups)

@group_required("admins", "seller")
def index(request):
    return HttpResponse("Hello METANIT.COM")
