from django.urls import path
from .import views

urlpatterns=[
    path('anihome',views.anihome,name='anihome'),
    path('createani',views.createani,name='createani'),
    path('updateani/<int:pk>',views.updateani,name='updateani'),
    path('deleteani/<int:pk>',views.deleteani,name='deleteani'),
]