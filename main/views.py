from django.shortcuts import render
from main.models import Facility,District,Taluka,Hospital,Availability,Headline
from django.views import generic
# Create your views here.




def index(request):

    headlines=Headline.objects.all()
    #services=Services.objects.all()
    selected_district_id=request.GET.get('district')
    selected_taluka_id=request.GET.get('taluka')
    selected_facility_id=request.GET.get('facility')


    if selected_district_id:
        talukas=Taluka.objects.filter(district=selected_district_id)
    else:
        talukas=Taluka.objects.all()


    hospitals=Hospital.objects.all()
    if selected_taluka_id:
        hospitals=hospitals.filter(taluka=Taluka(pk=selected_taluka_id))

    if selected_facility_id:
        availabilities=Availability.objects.all()
        if selected_taluka_id:
            availabilities=availabilities.filter(
                hospital__taluka=Taluka(pk=selected_taluka_id))

        availabilities=availabilities.filter(
            facility=Facility(pk=selected_facility_id),available__gt=0)

        hospitals=[]
        for avl in availabilities:
            hospitals.append(avl.hospital)

    facilities=Facility.objects.all().order_by('pk')
    
    districts=District.objects.all()
    
    context={
        #'services':services,
        'facilities':facilities,
        'districts':districts,
        'talukas':talukas,
        'hospitals':hospitals,
        'selected_district_id':selected_district_id,
        'selected_taluka_id':selected_taluka_id,
        'selected_facility_id':selected_facility_id,
        'headlines':headlines,
       
    }
    return render(request,template_name='main/index.html',context=context)

class HospitalDetailView(generic.DetailView):
    model=Hospital
