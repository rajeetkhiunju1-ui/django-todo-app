from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def task_list(request):
    task=Task.objects.all()
    context={"task":task}
    return render(request,"task.html",context)
def add_task(request):
    task=Task.objects.all()
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        T=Task.objects.create(
        title=title,
        description=description
        )
        return redirect('task_list')
    return render(request,"add_task.html")

def edit_task(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        task.title=title
        task.description=description
        task.save()
        return redirect("/task/")
    context={'task':task}
    return render(request,"task_edit.html",context)

def complete_task(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.is_completed=True
        task.save()
        return redirect('task_list')

def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('task_list')

