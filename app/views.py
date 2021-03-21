from django.shortcuts import render
from .models import emp
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from .forms import empForm,signin

class empCreateView(CreateView):
    form_class = empForm
    template_name = "create_view.html"

    success_url="/"

class empListView(ListView):
    model = emp
    template_name = "list_view.html"    

class empDetailView(DetailView):
    model = emp
    template_name = "detail_view.html"

class empUpdateView(UpdateView):
    model = emp
    fields = [ 
       "name","image","age","gender",
    ] 
    template_name = "update_view.html"  
    success_url = '/'

class empDeleteView(DeleteView):
    model = emp
    template_name = "delete_view.html"  
    success_url = '/'


class usercreate(CreateView):
    form_class = signin
    template_name = "signin.html"
    success_url = '/'