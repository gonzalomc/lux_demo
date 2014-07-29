from django.views.generic import ListView
from webapp.models.client import Client

class ClientListView(ListView):
    model = Client
    template_name = 'private/client/list.html'
    context_object_name = 'clients'
