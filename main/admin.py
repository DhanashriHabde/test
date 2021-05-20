from django.contrib import admin
from main.models import District, Facility,Taluka,Hospital,Availability,Headline#,Services
from django.dispatch import receiver
from django.db.models.signals import post_save



@receiver(post_save,sender=Hospital)
def afterHospitalSave(signal,instance,**kwargs):
    '''
    service=Services(hospital=instance)
    service.save()
    '''
    facilities=Facility.objects.all()
    for facility in facilities:
        availability=Availability(hospital=instance,facility=facility)
        availability.save()

@receiver(post_save,sender=Facility)
def afterHospitalSave(signal,instance,**kwargs):
    hospitals=Hospital.objects.all()
    for hospital in hospitals:
        availability=Availability(facility=instance,hospital=hospital)
        availability.save()

class FacilityAdmin(admin.ModelAdmin):
    model=Facility
    list_display=['title']
    

'''
class ServicesAdmin(admin.ModelAdmin):
    model=Services
    list_display=['hospital',
                  'oxygen_beds',
                  'oxygen_cylinder',
                  'ventilator'
                  ]

    def oxygen_beds(self,object):
        return f'{object.oxygen_beds_available}/{object.oxygen_beds_total}'

    def oxygen_cylinder(self,object):
        return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'

    def ventilator(self,object):
        return f'{object.ventilator_available}/{object.ventilator_total}'
'''

class HospitalAdmin(admin.ModelAdmin):
    model=Hospital
    list_display=['name','phone','address','taluka']

class AvailabilityAdmin(admin.ModelAdmin):
    model=Availability
    list_display=['hospital','facility','total','available','updated_at']
    list_editable=['total','available']

# Register your models here.
admin.site.register(District)
admin.site.register(Taluka)
admin.site.register(Hospital,HospitalAdmin)
#admin.site.register(Services,ServicesAdmin)
admin.site.register(Facility,FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)
admin.site.register(Headline)
