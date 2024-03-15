from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def index(request):
    home = models.Home.objects.all()
    about = models.AboutUs.objects.last()
    service = models.Service.objects.last()
    guard = models.Guards.objects.all()
    contact = models.Contact.objects.last()

    context = {
        'home': home,
        'about': about,
        'service': service,
        'guard': guard,
        'contact': contact,
    }
    return render(request, 'index.html', context)

def about(request):
    about = models.AboutUs.objects.last()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

def service(request):
    service = models.Service.objects.all()[:10] # Show only 10 latest services
    context = {
        'service' : service,
    }
    return render(request, 'service.html', context)

def guard(request):
    paginator = Paginator(models.Guards.objects.all(), 10) # Display 10 Guard objects per page
    page = request.GET.get('page')
    guard = paginator.get_page(page)

    context = {
        'guard' : guard,
    }
    return render(request, 'guard.html', context)

def contact(request):
    contact = models.Contact.objects.order_by('-created_at')[0]
    context = {
        'contact' : contact,
    }
    return render(request, 'contact.html', context)