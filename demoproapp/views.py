from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task

# Create your views here.


def todo(request):
    if request.method == 'POST':
        fm = TaskForm(request.POST)
        if fm.is_valid():
            task=fm.cleaned_data['task_title']
            desc=fm.cleaned_data['task_description']
            reg=Task(task_title=task,task_description=desc)
            reg.save()
            return redirect('todotask')
    else:
        fm = TaskForm()
    return render(request, 'homie.html', {'form': fm})


def details(request):
    stud = Task.objects.all()
    return render(request, 'todotask.html', {'stud': stud})

def reject(request,id):
    p1=Task.objects.get(pk=id)
    p1.delete()
    return redirect('todotask')
def updated(request,id):
    if request.method=='POST':
        p1=Task.objects.get(pk=id)
        fm=TaskForm(request.POST,instance=p1)
        if fm.is_valid():
            fm.save()
            return redirect('todotask')
    else:
        p1=Task.objects.get(pk=id)
        fm=TaskForm(instance=p1)
    return render(request,'edit.html',{'form':fm})

# Create your views here.
