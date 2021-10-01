from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse, Http404
from .models import Beacon, AlgilayiciModul, Oda
from .forms import BeaconForm, RoomForm, ModulForm
from django.contrib.auth.decorators import login_required
from personel.decorators import admin_only


# Create your views here.
@login_required(login_url='/login/')
@admin_only
def add_beacon(request):
    form = BeaconForm
    if request.method == "POST":
        form = BeaconForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_save = form.save()
            return HttpResponseRedirect(form_save.get_absolute_url_beacon())
    return render(request, 'beacon/add-beacon.html', context={'form': form})


@login_required(login_url='/login/')
@admin_only
def beacon_update(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    beacon = get_object_or_404(Beacon, pk=pk)
    form = BeaconForm(instance=beacon, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form_save = form.save()
        return HttpResponseRedirect(reverse('beacon-detail', kwargs={'pk': form_save.pk}))
    context = {'form': form, 'beacon': beacon}
    return render(request, 'beacon/beacon-update.html', context=context)


@login_required(login_url='/login/')
@admin_only
def beacon_delete(request, pk):
    beacon = get_object_or_404(Beacon, pk=pk)
    beacon.delete()
    return HttpResponseRedirect(reverse('beacon-list'))


@login_required(login_url='/login/')
@admin_only
def beacon_detail(request, pk):
    form = BeaconForm()
    try:
        beacon = Beacon.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'beacon/beacon-detail.html', context={'beacon': beacon, 'form': form})


@login_required(login_url='/login/')
@admin_only
def beacon_list(request):
    gelen_deger = request.GET.get('id', None)
    beacon = Beacon.objects.all()
    if gelen_deger:
        beacon = beacon.filter(pk=gelen_deger)
    context = {'beacon': beacon}
    return render(request, 'beacon/beacon-list.html', context)


@login_required(login_url='/login/')
@admin_only
def add_modul(request):
    form = ModulForm
    if request.method == "POST":
        form = ModulForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_save = form.save()
            return HttpResponseRedirect(form_save.get_absolute_url_modul())
    return render(request, 'beacon/add-modul.html', context={'form': form})


@login_required(login_url='/login/')
@admin_only
def modul_update(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    modul = get_object_or_404(AlgilayiciModul, pk=pk)
    form = ModulForm(instance=modul, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form_save = form.save()
        return HttpResponseRedirect(reverse('modul-detail', kwargs={'pk': form_save.pk}))
    context = {'form': form, 'modul': modul}
    return render(request, 'beacon/modul-update.html', context=context)


@login_required(login_url='/login/')
@admin_only
def modul_delete(request, pk):
    modul = get_object_or_404(AlgilayiciModul, pk=pk)
    modul.delete()
    return HttpResponseRedirect(reverse('modul-list'))


@login_required(login_url='/login/')
@admin_only
def modul_detail(request, pk):
    form = BeaconForm()
    try:
        modul = AlgilayiciModul.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'beacon/modul-detail.html', context={'modul': modul, 'form': form})


@login_required(login_url='/login/')
@admin_only
def modul_list(request):
    gelen_deger = request.GET.get('id', None)
    modul = AlgilayiciModul.objects.all()
    if gelen_deger:
        modul = modul.filter(pk=gelen_deger)
    context = {'modul': modul}
    return render(request, 'beacon/modul-list.html', context)


@login_required(login_url='/login/')
@admin_only
def add_room(request):
    form = RoomForm
    if request.method == "POST":
        form = RoomForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_save = form.save()
            return HttpResponseRedirect(form_save.get_absolute_url_room())
    return render(request, 'beacon/add-room.html', context={'form': form})


@login_required(login_url='/login/')
@admin_only
def room_update(request, pk):
    # if not request.user.is_authenticated:
    # return HttpResponseRedirect(reverse('user-login'))
    room = get_object_or_404(Oda, pk=pk)
    form = RoomForm(instance=room, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form_save = form.save()
        return HttpResponseRedirect(reverse('room-detail', kwargs={'pk': form_save.pk}))
    context = {'form': form, 'room': room}
    return render(request, 'beacon/room-update.html', context=context)


@login_required(login_url='/login/')
@admin_only
def room_delete(request, pk):
    room = get_object_or_404(Oda, pk=pk)
    room.delete()
    return HttpResponseRedirect(reverse('room-list'))


@login_required(login_url='/login/')
@admin_only
def room_detail(request, pk):
    form = ModulForm()
    try:
        room = Oda.objects.get(pk=pk)
    except:
        raise Http404
    return render(request, 'beacon/room-detail.html', context={'room': room, 'form': form})


@login_required(login_url='/login/')
@admin_only
def room_list(request):
    gelen_deger = request.GET.get('id', None)
    room = Oda.objects.all()
    if gelen_deger:
        room = room.filter(pk=gelen_deger)
    context = {'room': room}
    return render(request, 'beacon/room-list.html', context)
