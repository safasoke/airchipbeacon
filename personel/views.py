from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse, Http404, HttpResponse
from .models import Personeller
from .forms import PersonnelForm, TaskForm, PersonnelSearch
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


# Create your views here.

def add_personnel(request):
    form = PersonnelForm
    if request.method == "POST":
        form = PersonnelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form_save = form.save()
            msg = "%s isimli personel başarıyla eklendi." % (form_save.isim)
            return HttpResponseRedirect(form_save.get_absolute_url())
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
