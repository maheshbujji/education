"""projeect1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

from app1 import views
from app1.views import viewlist, Maheshupdate, maheshdelete, Facultysave

urlpatterns = [
    path('',views.showindex),
    path('login/',views.display),
    path('mahesh/',views.save),
    path('views/',viewlist.as_view(),name='name'),
    path('update/<str:pk>/',Maheshupdate.as_view()),
    path('delete/<str:pk>/',maheshdelete.as_view()),
    path('register/',views.register),
    path('maheshg/',views.registerfaculty),
    path('maheshfaculty/',views.Facuityregister),
    path('viewsfaculty/',Facultysave.as_view()),
    path('ramu/',views.search),
    path('Suggestions/',views.Suggestions),
    path('library/',views.Openlibrary),
    path('maa/',views.Books),
    path('studentlogin/',views.studentlogin),
    path('loginstudent/',views.loginstudent),
    path('facultylogin/',views.facultylogin),
    path('attendenc/',views.reports),
    path('saveattendenc/',views.AttedenceSave),

   #
]
