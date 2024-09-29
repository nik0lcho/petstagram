from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, 'accounts/register-page.html')


def login(request):
    return render(request, 'accounts/login-page.html')


def show_profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html', {'pk': pk})


def edit_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html', {'pk': pk})


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html', {'pk': pk})
