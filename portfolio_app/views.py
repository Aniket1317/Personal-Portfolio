from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
	projects = Project.objects.all() 
	return render(request,'portfolio_app/home.html', {'projects':projects})