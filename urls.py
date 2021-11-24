from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'general'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^validate', views.validate, name = 'validate'),
    url(r'^signup', views.signup, name = 'signup'),
    url(r'^createUser', views.createUser, name = 'createUser')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)