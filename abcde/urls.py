"""todo_upgrad URL Configuration

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
from django.conf import settings
from django.urls import path,include
from abcd.views import register_view, user_login, user_logout, add_task, show ,destroy , crossoff, uncross
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_view/', register_view, name="register_view"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('', show, name='show'),
    path('add_task', add_task, name= 'add_task'),
    path('show',show,name='show'),
    path('delete/<int:id>',destroy,name='destroy'),
    path('crossoff/<int:id>',crossoff,name = 'crossoff'),
    path('uncross/<int:id>',uncross,name = 'uncross'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema),name='graphql'),
    path('api/', include('api.urls')),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)