from django.shortcuts import render,redirect
from .models import Todo
from django.views.decorators.http import require_POST

from .forms import TodoForm
# Create your views here.

def index(request):
    # if request.method == 'POST':
    #     todoForm = TodoForm(request.POST)
    #     if todoForm.is_valid():

    #         #save the requested data in db
    #         new_todo = Todo(text = request.POST['text'])
    #         new_todo.save()
    #         return redirect('IndexView')
        
    # else:
    form = TodoForm ()

    
    todos = Todo.objects.all().order_by('-id')
    context = {'todos': todos, 'form':form}
    return render(request,'initial_app/index.html',context)

@require_POST
def save_data(request):
    todoForm = TodoForm(request.POST)
    if todoForm.is_valid():

         #save the requested data in db
        new_todo = Todo(text = request.POST['text'])
        new_todo.save()
    return redirect('IndexView')

def makeComplete(request,todo_id):
    pendingTodo = Todo.objects.get(pk=todo_id)
    pendingTodo.isComplete = True
    pendingTodo.save()
    return redirect('IndexView')

def makePending (request, todo_id):
    completedTodo = Todo.objects.get(pk=todo_id)
    completedTodo.isComplete = False
    completedTodo.save()
    return redirect('IndexView')

def deleteCompleted(request):
    completed_todos = Todo.objects.filter(isComplete__exact = True).delete()
    return redirect('IndexView')


def deleteAll(request):
    all_todos = Todo.objects.all().delete()
    return redirect('IndexView')