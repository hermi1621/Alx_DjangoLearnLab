from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Views with access restrictions using @user_passes_test

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'django_models/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'django_models/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'django_models/member_view.html')
