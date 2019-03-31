from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ProfessorForm
# Create your views here.

@login_required
def professors_list_view(request):
    queryset = User.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "professor/display_all.html", context)

@login_required
def professor_create_view(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfessorForm()
    context = {
        'form': form
    }
    return render(request, "professor/create.html", context)