from django.shortcuts import render, redirect
from django.http import HttpResponse

from artists.models import Artist
from .forms import ArtistForm
from django.contrib import messages

# Create your views here.

def index(request):
    artists = Artist.objects.all()

    return render(request, 'artists/artists.html', {'artists' : artists})

def create_artist(request):
    form = ArtistForm()

    if request.method == "POST":
        form = ArtistForm(request.POST)
        stage_name = request.POST.get('stage_name')
        if form.is_valid:
            try:
                artist = Artist.objects.get(stage_name = stage_name)
            except:
                form.save()
                return redirect('artists')
    context = {'form': form}

    return render(request, 'artists/artist_form.html', context)