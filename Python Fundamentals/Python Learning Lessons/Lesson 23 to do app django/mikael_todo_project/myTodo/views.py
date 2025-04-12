from django.shortcuts import render
from .models import Todo
# Create your views here.
def home (request):
    data = Todo.objects.all()
    return render(request, 'index.html',{'data_all':data})