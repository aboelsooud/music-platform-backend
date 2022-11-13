from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from artists.models import Artist
from .forms import ArtistForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(TemplateView):
    template_name = 'artists/artists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artists'] = Artist.objects.all()
        return context

class CreateArtistView(LoginRequiredMixin, View):
    form_class = ArtistForm
    initial = {'key': 'value'}
    template_name = 'artists/artist_form.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        stage_name = request.POST.get('stage_name')
        if form.is_valid:
            try:
                artist = Artist.objects.get(stage_name = stage_name)
            except:
                form.save()
                return redirect('artists')
        context = {'form': form}
        return render(request, 'artists/artist_form.html', context)
