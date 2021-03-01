from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Blog
from CurriculumVitae.models import CV
from django.views.generic import TemplateView

# Create your views here.

class BlogListView(ListView):
    model=Blog
    template_name='cv-information.html'

class AnasayfaView(TemplateView):
    template_name="home.html"

class CreateCvView(ListView):
    model=CV
    template_name="create-cv.html"