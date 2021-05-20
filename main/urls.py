from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('hospital/<int:pk>',views.HospitalDetailView.as_view(),name="hospitaldetail")
]
