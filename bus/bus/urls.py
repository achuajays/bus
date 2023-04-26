"""bus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buss',views.buss,name="buss"),
    path('busv',views.busv,name="busv"),
    path('reg/<int:id>/',views.regs,name="regs"),
    path('',views.login,name="login"),
    path('register',views.register,name="register"),
    path('ticket',views.ticket,name="ticket"),
    path('file',views.my_csv_view,name="file"),
    path('my_text_file_view/<int:id>/',views.my_text_file_view,name="my_text_file_view"),


]
