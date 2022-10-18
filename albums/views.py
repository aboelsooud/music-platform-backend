from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AlbumForm

# Create your views here.

def index(request):
    return HttpResponse('album')

def create_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('albums')
    context = {'form' : form}

    return render(request, 'albums/album_form.html', context)