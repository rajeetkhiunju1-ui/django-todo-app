"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import *
urlpatterns = [
    path('',task_list,name="task_list"),
    path('task/',task_list,name='task_list'),
    path('task/add/',add_task,name="add_task"),
    path('task/<int:id>/edit/',edit_task,name="edit_task"),
    path('task/<int:id>/complete/',complete_task,name="complete_task"),
    path('task/<int:id>/delete/',delete_task,name="delete_task"),
    path('admin/', admin.site.urls),
    ]
