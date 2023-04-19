from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse

def main_page(request):
	todos = Todo.objects.all()
	return render(request, "todo/index.html", {"todos": todos})
