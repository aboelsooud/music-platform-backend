from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArtistForm

# Create your views here.

def index(request):
    return HttpResponse("artist")

def create_artist(request):
    form = ArtistForm()

    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('artists')


    context = {'form': form}

    return render(request, 'artists/artist_form.html', context)