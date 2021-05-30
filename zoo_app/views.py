from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
import time

# Create your views here.
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404


class Register(View):
    def get(self, *args, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(self.request, 'register.html', context)

    def post(self, *args, **kwargs):
        form = UserCreationForm(self.request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(self.request, user)
            time.sleep(1)
            return redirect('index')
        else:
            messages.info(self.request, 'Ошибка регистрации! Проверьте поля!')
            return HttpResponseRedirect('register')


class Out(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('index')


class Index(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')


class AviaryIndex(View):
    def get(self, *args, **kwargs):
        aviary = Aviary.objects.order_by()
        return render(self.request, 'aviary/index.html', {'aviary': aviary})


class AnimaliaIndex(View):
    def get(self, *args, **kwargs):
        animalia = Animalia.objects.order_by()
        return render(self.request, 'animalia/index.html', {'animalia': animalia})


class AnimalIndex(View):
    def get(self, *args, **kwargs):
        animal = Animal.objects.order_by()
        return render(self.request, 'animal/index.html', {'animal': animal})


class AdminIndex(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return render(self.request, 'adminpanel/index.html')
        else:
            return render(self.request, 'adminpanel/accessDenie.html')


class CreateAviary(View):
    def get(self, *args, **kwargs):
        form = CreateAviaryForm()
        return render(self.request, 'adminpanel/add_aviary.html', {'form': form})

    def post(self, *args, **kwargs):
        form = CreateAviaryForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            aviary = form.save(commit=False)
            aviary.createSlug()
            aviary.save()
            return redirect('index')
        else:
            return render(self.request, 'adminpanel/add_aviary.html')


class CreateAnimalia(View):
    def get(self, *args, **kwargs):
        form = CreateAnimaliaForm()
        return render(self.request, 'adminpanel/add_animalia.html', {'form': form})

    def post(self, *args, **kwargs):
        form = CreateAnimaliaForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            animalia = form.save(commit=False)
            animalia.createSlug()
            animalia.save()
            print(animalia.img)
            return redirect('index')
        else:
            return render(self.request, 'adminpanel/add_animalia.html')


class CreateAnimal(View):
    def get(self, *args, **kwargs):
        form = CreateAnimalForm()
        return render(self.request, 'adminpanel/add_animal.html', {'form': form})

    def post(self, *args, **kwargs):
        form = CreateAnimalForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.createSlug()
            animal.save()
            print(animal.img)
            return redirect('index')
        else:
            return render(self.request, 'adminpanel/add_animal.html')




class DeleteAviary(View):
    def get(self, *args, **kwargs):
        av = get_object_or_404(Aviary, slug=kwargs['slug'])
        av.delete()
        return redirect('index')



class DeleteAnimalia(View):
    def get(self, *args, **kwargs):
        av = get_object_or_404(Animalia, slug=kwargs['slug'])
        av.delete()
        return redirect('index')


class DeleteAnimal(View):
    def get(self, *args, **kwargs):
        av = get_object_or_404(Animal, slug=kwargs['slug'])
        av.delete()
        return redirect('index')