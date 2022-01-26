from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .models import Client, Massage, Service
from .forms import ServiceForm

def home(request):
    # """View function for home page of site."""
    #
    # # Generate counts of some of the main objects
    # # num_books = Book.objects.all().count()
    # num_clients = Client.objects.all().count()
    # # num_instances = BookInstance.objects.all().count()
    # num_massages = Massage.objects.all().count()
    #
    # # Available books (status = 'a')
    # # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_clients_yann = 0 #Client.objects.filter(client_first_name__icontains='yann').count()
    #
    # # The 'all()' is implied by default.
    # # num_authors = Author.objects.count()
    # num_services = Service.objects.all().count()
    #
    # context = {
    #     'num_clients': num_clients,
    #     'num_massages': num_massages,
    #     'num_services': num_services,
    #     'num_clients_yann': num_clients_yann,
    # }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home.html')#, context=context)

def list_clients(request):
    client_list = Client.objects.all()
    return render(request, 'clients/list_clients.html', {'client_list': client_list})

def list_massages(request):
    massage_list = Massage.objects.all()
    return render(request, 'massages/list_massages.html', {'massage_list': massage_list})

def list_services(request):
    service_list = Service.objects.all()
    return render(request, 'services/list_services.html', {'service_list': service_list})

def add_client(request):
    form = Client
    return render(request, 'clients/add_client.html', {'form': form})

def add_service(request):
    submitted = False
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_service?submitted=True')
    else:
        form = ServiceForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'services/add_service.html', {'form': form, 'submitted': submitted})

def show_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    return render(request, 'clients/show_client.html', {'client': client})

