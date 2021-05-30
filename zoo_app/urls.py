from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path(r'register', Register.as_view(), name='register'),
    path(r'out', Out.as_view(), name='out'),
    path(r'adminpanel/index', AdminIndex.as_view(), name='adminpanel'),
    path(r'adminpanel/add_aviary', CreateAviary.as_view(), name='createaviary'),
    path(r'deleteaviary/<slug>', DeleteAviary.as_view(), name='deleteaviary'),
    path(r'adminpanel/add_animalia', CreateAnimalia.as_view(), name='createanimalia'),
    path(r'deleteanimalia/<slug>', DeleteAnimalia.as_view(), name='deleteanimalia'),
    path(r'adminpanel/add_animal', CreateAnimal.as_view(), name='createanimal'),
    path(r'deleteanimal/<slug>', DeleteAnimal.as_view(), name='deleteanimal'),
    path(r'aviary/index', AviaryIndex.as_view(), name='aviaryindex'),
    path(r'animalia/index', AnimaliaIndex.as_view(), name='animaliaindex'),
    path(r'animal/index', AnimalIndex.as_view(), name='animalindex'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


