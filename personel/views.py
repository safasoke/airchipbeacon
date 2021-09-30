from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse, Http404, HttpResponse
from .models import Personeller
from .forms import PersonnelForm, TaskForm, PersonnelSearch, RegisterForm, LoginForm, UserPasswordChangeForm2, UserProfileUpdateForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .decorators import is_anonymous_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def add_personnel(request):
    form = [PersonnelForm, RegisterForm]

    if request.method == "POST":
        form2 = PersonnelForm(data=request.POST, files=request.FILES)
        form1 = RegisterForm(data=request.POST or None)
        if form1.is_valid() and form2.is_valid():
            personnels = form2.save()
            user = form1.save(commit=False)
            password = form1.cleaned_data.get('password')
            username = form1.cleaned_data.get('username')
            user.set_password(password)
            user.save()
            userprofile = UserProfile.objects.create(user=user)
            user.userprofile = userprofile
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, '<b>Kayıt olundu</b>', extra_tags='success')
                    return HttpResponseRedirect(user.userprofile.get_user_profile_url())
            return HttpResponseRedirect(personnels.get_absolute_url())
    return render(request, 'personel/add-personnel.html', context={'form': form})


def add_task(request, pk):
    personel = get_object_or_404(Personeller, pk=pk)
    form = TaskForm(data=request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.personel = personel
        new_task.save()
        return HttpResponseRedirect(reverse('personnel-detail', kwargs={'pk': personel.pk}))


def personnel_detail(request, pk):
    form = TaskForm()
    try:
        personel = Personeller.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'personel/personnel-detail.html', context={'personel': personel, 'form': form})


def personnel_update(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    personel = get_object_or_404(Personeller, pk=pk)
    form = PersonnelForm(instance=personel, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form_save = form.save()
        return HttpResponseRedirect(reverse('personnel-detail', kwargs={'pk': form_save.pk}))
    context = {'form': form, 'personel': personel}
    return render(request, 'personel/personnel-update.html', context=context)


def personnel_delete(request, pk):
    personel = get_object_or_404(Personeller, pk=pk)
    personel.delete()
    return HttpResponseRedirect(reverse('personnel-list'))

@login_required(login_url='/login/')
def personnel_list(request):
    gelen_deger = request.GET.get('id', None)
    personeller = Personeller.objects.all()
    form = PersonnelSearch(data=request.GET or None)
    if form.is_valid():
        search = form.cleaned_data.get('search', None)
        if search:
            personeller = personeller.filter(
                Q(isim__icontains=search) | Q(soyisim__icontains=search) | Q(tc_kimlik_no__icontains=search))
    page = request.GET.get('page', 1)
    if gelen_deger:
        personeller = personeller.filter(pk=gelen_deger)
    paginator = Paginator(personeller, 20)
    try:
        personeller = paginator.page(page)
    except EmptyPage:
        personeller = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        personeller = paginator.page(1)
    return render(request, 'personel/personnel-list.html', context={'personeller': personeller, 'form': form})


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        personnel = Personeller.objects.filter(isim__icontains=q)
        results = []
        for pl in personnel:
            personnel_json = {}
            personnel_json = pl.isim + " " + pl.soyisim
            results.append(personnel_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@is_anonymous_required
def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = form.cleaned_data.get('username')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                msg = '<b>Merhaba %s hoşgeldin</b>' % username
                messages.success(request, msg, extra_tags='success')
                return HttpResponseRedirect(reverse('personnel-list'))
    return render(request, 'personel/login.html', context={'form': form})

def user_logout(request):
    username = request.user.username
    logout(request)
    msg = '<b>%s</b> hesabından çıkış yapıldı. ' % username
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('user-login'))

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    #user_post_list = Post.objects.filter(user=user)
    return render(request, 'personel/profile/user-profile-page.html',
                  context={'user': user})

def user_settings(request):
    bio = request.user.userprofile.bio
    profile_photo = request.user.userprofile.profile_photo
    initial = {'bio': bio, 'profile_photo': profile_photo}
    form = UserProfileUpdateForm(initial=initial, instance=request.user, data=request.POST or None,
                                 files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=True)
            bio = form.cleaned_data.get('bio', None)
            profile_photo = form.cleaned_data.get('profile_photo', None)
            user.userprofile.bio = bio
            user.userprofile.profile_photo = profile_photo
            user.userprofile.save()
            messages.success(request, 'Profiliniz başarıyla güncellendi', extra_tags='success')
            return HttpResponseRedirect(reverse('user-profile', kwargs={'username': user.username}))
        else:
            messages.warning(request, 'Lütfen girdiğiniz bilgileri kontrol ediniz', extra_tags='danger')

    return render(request, 'personel/profile/user-settings.html', context={'form': form})

def user_about(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'personel/profile/user-aboutme.html', context={'user': user})

def user_password_change(request):
    # form = UserPasswordChangeForm(user=request.user, data=request.POST or None)
    form = UserPasswordChangeForm2(user=request.user, data=request.POST or None)  # Django PasswordChangeForm
    if form.is_valid():
        # new_password = form.cleaned_data.get('new_password')
        # request.user.set_password(new_password)
        # request.user.save()
        user = form.save(commit=True)  # Django PasswordChangeForm
        update_session_auth_hash(request, user)  # Django PasswordChangeForm
        update_session_auth_hash(request, request.user)
        messages.success(request, 'Şifreniz başarıyla güncellendi', extra_tags='success')
        return HttpResponseRedirect(reverse('user-profile', kwargs={'username': request.user.username}))
    return render(request, 'personel/profile/user-password-change.html', context={'form': form})

