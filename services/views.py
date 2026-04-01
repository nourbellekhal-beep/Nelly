from django.shortcuts import render
from .models import Service, Category

def service_list(request):
    categories = Category.objects.all()
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services, 'categories': categories})
