from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import Todo
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class tasklist(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'taskdetails'

class detailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'
class updateview(UpdateView):

    model = Task
    template_name = 'update.html'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('list',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

# Create your views here.
def add(request):
   taskdetails=Task.objects.all()
   if request.method=='POST':
       name=request.POST.get('name',)
       priority=request.POST.get('priority',)
       date=request.POST.get('date',)
       task=Task(name=name,priority=priority,date=date)
       task.save()
   return render(request,'home.html',{'taskdetails':taskdetails})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form=Todo(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})
