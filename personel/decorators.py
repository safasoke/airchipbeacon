from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import reverse, render



def is_post(func):
    def wrap(request, *args, **kwargs):
        if request.method == 'GET':
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)

    return wrap


def is_anonymous_required(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('personnel-list'))
        return func(request, *args, **kwargs)

    return wrap


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('You are not authorized to view this page')

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'personnel':
            return render(request, 'personel/profile/user-profile-page.html')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
