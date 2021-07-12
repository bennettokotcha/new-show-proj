from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):
    return redirect('/shows')

def add_show(request):
    return render(request, 'add_show.html')

def create_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0 :
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/shows/new')
    else:
        create_show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        return redirect(f'/shows/{create_show.id}')

def show_details(request, number):
    context = {
        'all_shows' : Show.objects.all(),
        'create_show' : Show.objects.get(id=number)
    }
    return render(request, 'show_details.html', context)

def shows(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

def edit(request, number):
    context = {
        'all_shows' : Show.objects.all(),
        'edit_show' : Show.objects.get(id=number)
    }
    return render(request, 'edit_shows.html', context)

def make_changes(request, number):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0 :
        for k,v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/{number}/edit')
    else:    
        edit_show = Show.objects.get(id=number)
        edit_show.title=request.POST['title']
        edit_show.network=request.POST['network']
        edit_show.release_date=request.POST['release_date']
        edit_show.desc=request.POST['desc']
        edit_show.save()
        return redirect(f'/shows/{edit_show.id}')

def delete_show(request, number):
    this_show = Show.objects.get(id=number)
    this_show.delete()
    return redirect('/shows')
# Create your views here.
