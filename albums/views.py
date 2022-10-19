from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AlbumForm
from dateutil.parser import parse

# Create your views here.

def index(request):
    return HttpResponse('album')

def create_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        realease_date = request.POST.get('release_date')
        if form.is_valid:
            try:
                parse(realease_date)
                form.save()
                return redirect('albums')
            except:
                pass
    context = {'form' : form}

    return render(request, 'albums/album_form.html', context)
