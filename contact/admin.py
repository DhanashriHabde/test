from django.contrib import admin
from contact.models import Contact,Plasma,Ambulance


class ContactAdmin(admin.ModelAdmin):
    model=Contact
    list_display=['name','phone','created_at']

class PlasmaAdmin(admin.ModelAdmin):
    model=Plasma
    list_display=['name','phone','bloodgroup','created_at','last_donated_on']


class AmbulanceAdmin(admin.ModelAdmin):
    model=Plasma
    list_display=['name','phone','paid']
    
# Register your models here.
admin.site.register(Contact,ContactAdmin)
admin.site.register(Plasma,PlasmaAdmin)
admin.site.register(Ambulance,AmbulanceAdmin)