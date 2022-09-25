from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from .models import Vessel

from django.core.cache import cache


class VesselView(View):

    def get(self, request):
        template = 'home.html'
        vessels = Vessel.objects.all()
        context = {'vessels': vessels}

        return render(request, template, context)


class AboutView(View):
    template = 'about.html'

    def get(self, request, *args, **kwargs):
        vessel_id = kwargs['pk']
        if cache.get(vessel_id):
            vessel = cache.get(vessel_id)
            print('hit the cache')
        else:
            try:
                vessel = Vessel.objects.get(pk=vessel_id)
                cache.set(vessel_id, vessel)
                print('hit the db')
            except ObjectDoesNotExist:
                return HttpResponse('Vessel does not exist!')

        context = {'vessel': vessel}
        return render(request, self.template, context)
