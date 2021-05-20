from django import template
from main.models import Availability

register=template.Library()

@register.simple_tag
def get_table_class(value):
    if value:
        return 'bg-success'
    else:
        return 'bg-danger text-light'

@register.simple_tag
def get_availabilities(hospital):
    return Availability.objects.filter(hospital=hospital).order_by('facility_id')

@register.simple_tag
def is_option_selected(selected_option,pk):
    if selected_option==str(pk):
        return 'selected'
    else:
        return ''

