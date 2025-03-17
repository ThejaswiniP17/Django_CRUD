from django.urls import path
from .import views

urlpatterns=[
   path('birdhome',views.home,name='birdhome'),
   path('createbd',views.create,name='createbd'),
   path('updatebd/<int:pk>',views.updatebd,name='updatebd'),
   path('deletebd/<int:pk>',views.deletebd,name='deletebd'),

]