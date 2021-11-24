from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'loggedin'

urlpatterns = [
    url(r'^tasks', views.tasks, name = 'tasks'),
    url(r'^addtask', views.addtask, name = 'addtask'),
    url(r'^signout', views.signout, name = 'signout'),
    url(r'^insert', views.insert, name = 'insert'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^midupdate/(?P<id>\d+)$', views.midupdate, name='midupdate'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
]