from django.shortcuts import render
from services.models import Service

def home(request):
    featured_services = Service.objects.all()[:3]
    return render(request, 'base/home.html', {'featured_services': featured_services})
