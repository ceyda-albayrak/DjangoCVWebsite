from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import DetailView,ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import CV
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

# Create your views here.
class AnasayfaView(TemplateView):
    template_name="home.html"

class ViewCV(LoginRequiredMixin,DetailView):
    model=CV
    template_name="view-cv.html"
   
class CVCreateView(CreateView):
    model=CV
    template_name="create-cv.html"
    fields="__all__"

class CvList(ListView):
    model=CV
    template_name="cv-list.html"

class UpdateCV(UpdateView):
    model=CV
    template_name="cv-update.html"
    fields="__all__"

class DeleteCV(DeleteView): 
    model=CV
    template_name="cv-delete.html"
    success_url=reverse_lazy('cv-list')
   
