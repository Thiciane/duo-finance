from django.urls import path
from . import views
from . import urls

urlpatterns = [path(view_path,fn,name=name) for view_path, fn, name in urls]