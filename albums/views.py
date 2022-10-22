from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AlbumForm
from dateutil.parser import parse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(View):

    def get(self, request):
        return HttpResponse('album')


class CreateAlbumView(LoginRequiredMixin ,View):
    form_class = AlbumForm
    initial = {'key': 'value'}
    template_name = 'albums/album_form.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
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
