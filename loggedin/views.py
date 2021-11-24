from django.shortcuts import render, redirect, reverse
from .models import Tasks
from general.models import User
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
def tasks(req):
    try:
        if req.session['userid']:
            v = Tasks.objects.all().filter(userid = req.session['userid'])
            x = User.objects.get(id = req.session['userid'])
            print(MEDIA_ROOT)
            x = os.path.join(MEDIA_ROOT,x.image)
            return render(req,'tasks.html', {'v': v, 'x': x})
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def signout(req):
    try:
        if req.session['userid']:
            del req.session['userid']
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def addtask(req):
    try:
        if req.session['userid']:
            return render(req,'addtask.html')
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def insert(req):
    try:
        print(req.session['userid'])
        if req.session['userid']:
            task = req.POST['task']
            c = Tasks(task = task, userid = req.session['userid'])
            c.save()
            # v = Tasks.objects.all.filter(userid = req.session['userid'])
            # print(v)
            return redirect('loggedin:tasks')
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def delete(req, id):
    try:
        print(req.session['userid'])
        if req.session['userid']:
            v = Tasks.objects.filter(id = id)
            v.delete()
            return redirect('loggedin:tasks')
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def midupdate(req, id):
    try:
        if req.session['userid']:
            v = Tasks.objects.all().filter(id = id)
            return render(req, 'updateTask.html', {'v': v[0]})
    except KeyError:
        pass
    return redirect(reverse('general:index'))

def update(req, id):
    try:
        print(req.session['userid'])
        if req.session['userid']:
            v = Tasks.objects.get(id = id)
            v.task = req.POST['task']
            v.save()
            return redirect('loggedin:tasks')
    except KeyError:
        pass
    return redirect(reverse('general:index'))