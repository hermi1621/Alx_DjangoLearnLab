from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'django_models/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'django_models/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'django_models/member_view.html')
