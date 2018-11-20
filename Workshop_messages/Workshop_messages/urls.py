"""Workshop_messages URL Configuration

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
from django.urls import path, re_path

from Messages_server.views import add_person, delete_person, show_person, show_all, MainView, \
    ModifyPerson, AddTelephone, AddEmail, AddAdress, show_all_groups, AddContactToGroup, GroupSearch, PersonInGroups

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^new$', add_person),
    re_path(r'^modify/(?P<id>\d+)$', ModifyPerson.as_view()),
    re_path(r'^(?P<id>\d+)/[a,d]{3}[A]\D{4}[s]$', AddAdress.as_view()),
    re_path(r'^(?P<id>\d+)/addEmail$', AddEmail.as_view()),
    re_path(r'^(?P<id>\d+)/addTelephone$', AddTelephone.as_view()),
    re_path(r'^delete/(?P<id>\d+)$', delete_person),
    re_path(r'^show/(?P<id>\d+)$', show_person),
    re_path(r'^$', MainView.as_view()),
    re_path(r'^allusers$', show_all),
    re_path(r'^allGroups', show_all_groups),
    re_path(r'^AddContactToGroup', AddContactToGroup.as_view()),
    re_path(r'^groupSearch', GroupSearch.as_view()),
    re_path(r'^personInGroups', PersonInGroups.as_view())
]
