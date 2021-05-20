from django.shortcuts import reverse
from django.views import generic
from contact.models import Contact,Plasma,Ambulance
# Create your views here.
class ContactCreateView(generic.CreateView):
    model=Contact
    fields=['name','phone','text','emergency']

class PlasmaCreateView(generic.CreateView):
    model=Plasma
    fields=['name','phone','bloodgroup']

class AmbulanceListView(generic.ListView):
    model=Ambulance
    fields=['name','phone','organization','paid']
    context_object_name ='ambulances'