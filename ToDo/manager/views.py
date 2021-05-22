from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from datetime import datetime
# Create your views here.
now = datetime.now()
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        todo = ToDo()
        lenght = int(len(ToDo.objects.all()))
        print(lenght)
        todo.sno = lenght + 1
        todo.title=title
        todo.date_created = str(now.strftime("%H:%M:%S"))
        todo.desc=desc
        todo.save()
    allTodo = ToDo.objects.all()
    return render(request,'index.html', {'allTodo':allTodo})
def products(request):
    allTodo = ToDo.objects.all()
    print(allTodo)
    return 'this is products page'


def update(request,sno):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        lenght = len(ToDo.objects.all())
        print(lenght)
        todo = ToDo.objects.filter(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.date_created = str(now.strftime("%H:%M:%S"))
        todo.save()
        return redirect("/")

    todo = ToDo.objects.filter(sno=sno).first()
    return render(request,'update.html', {'todo':todo})
def delete(request,sno):
    todo = ToDo.objects.filter(sno=sno).first()
    todo.delete()
    return redirect("/")
