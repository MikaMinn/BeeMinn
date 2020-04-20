from datetime import datetime
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Hives, Zones, History
from .forms import AddHistory, AddHive, AddZone, ParagraphErrorList, SignUpForm, CustomAuthForm
from .filters import HivesFilter

datetime.now()

@login_required
def index(request):
    return redirect('hives:hives')

@login_required
def hives(request):
    context = {
        'hives': Hives.objects.all(),
        'zones': Zones.objects.filter(user=request.user),
    }
    return render(request, 'hives/my_hives.html', context)

@login_required
def detail(request, hive_id):
    hive = get_object_or_404(Hives, pk=hive_id)
    form = AddHistory()
    context = {
        'hive': hive,
        'form': form,
    }
 
    if request.method == 'POST':
        form = AddHistory(request.POST)
        if form.is_valid():
            details = form.cleaned_data['details']
            created_at = form.cleaned_data['created_at']
            history = History.objects.create(details = details, created_at = created_at, hive_id = hive_id)
            history.save()  
            return HttpResponseRedirect(request.path)
        else:
            context['errors'] = form.errors.items()

        context['form'] = form
    
    return render(request, 'hives/detail.html', context)

@login_required
def delete_history(request, history_id, hive_id):
    object = History.objects.get(id=history_id)
    object.delete()
    hive = get_object_or_404(Hives, pk=hive_id)
    form = AddHistory()
    context = {
        'hive': hive,
        'form': form,
    }
    return redirect('hives:detail', hive_id=hive_id)

@login_required
def add_hive(request):
    form = AddHive()
    form.fields["zone"].queryset = Zones.objects.filter(user=request.user)
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = AddHive(request.POST)
        if form.is_valid():
            hive_add = form.save(commit=False)
            hive_add.user = request.user
            hive_add = form.save()
            return redirect('hives:hives')
            
        else:
            context['errors'] = form.errors.items()
            return render(request, 'hives/add_hive.html', context)
    
    return render(request, 'hives/add_hive.html', context)

@login_required
def edit_hive(request, hive_id):
    object = Hives.objects.get(id=hive_id)
    if object.user == request.user :
        hive = Hives.objects.get(pk=hive_id)
        form = AddHive(instance=hive)
        form.fields["zone"].queryset = Zones.objects.filter(user=request.user)
        edit_mode = True
        context = {
            'form': form,
            'edit_mode' : edit_mode,
            'hive' : hive,
        }

        if request.method == 'POST':
            form = AddHive(request.POST, instance=hive)
            if form.is_valid():
                form.save()
                return redirect('hives:hives')
            else:
                context['errors'] = form.errors.items()
                return render(request, 'hives/add_hive.html', context)


        return render(request, 'hives/add_hive.html', context)        
    else:
        return redirect('hives:hives')

@login_required
def zone(request):
    form = AddZone()
    button_title = "Ajouter la zone"
    title = "Mes zones"
    context = {
        'form': form,
        'zones': Zones.objects.filter(user=request.user),
        'button_title' : button_title,
        'title' : title
    }

    if request.method == 'POST':
        form = AddZone(request.POST)
        if form.is_valid():
            zone_add = form.save(commit=False)
            zone_add.user = request.user
            zone_add.save()
            return redirect('hives:hives')
            
        else:
            context['errors'] = form.errors.items()
            return render(request, 'hives/zone.html', context)


    return render(request, 'hives/zone.html', context)

@login_required
def edit_zone(request, zone_id):
    object = Zones.objects.get(id=zone_id)
    if object.user == request.user :
        zone = Zones.objects.get(pk=zone_id)
        form = AddZone(instance=zone)
        button_title = "Modifier la zone"
        title = "Modifier la zone : " + zone.name
        context = {
            'form': form,
            'zones': Zones.objects.filter(user=request.user),
            'button_title' : button_title,
            'title' : title,
        }

        if request.method == 'POST':
            form = AddZone(request.POST, instance=zone)
            if form.is_valid():
                zone_add = form.save(commit=False)
                zone_add.user = request.user
                zone_add.save()
                return redirect('hives:hives')
                
            else:
                context['errors'] = form.errors.items()
                return render(request, 'hives/zone.html', context)


        return render(request, 'hives/zone.html', context)  
    else:
        return redirect('hives:hives')

@login_required
def delete_hive(request, hive_id):
    object = Hives.objects.get(id=hive_id)
    if object.user == request.user :
        object.delete()
        return redirect('hives:hives')
    else :
        return redirect('hives:hives')
   
@login_required
def delete_zone(request, zone_id):
    object = Zones.objects.get(id=zone_id)
    if object.user == request.user :
        object = Zones.objects.get(id=zone_id)
        object.delete()
        return redirect('hives:zones')
    return redirect('hives:zones')

@login_required
def search(request):
    
    hives = Hives.objects.filter(user=request.user)
    myFilter = HivesFilter(request.GET, queryset=hives)
    myFilter.filters["zone"].queryset = Zones.objects.filter(user=request.user)
    hives = myFilter.qs 
    context = {
        'myFilter':myFilter,
        'hives':hives
        }
    return render(request, 'hives/result_search.html', context)

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            return redirect("/hives/")
    else:
        form = SignUpForm()
    return render(request, "hives/register.html", {"form": form})

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))