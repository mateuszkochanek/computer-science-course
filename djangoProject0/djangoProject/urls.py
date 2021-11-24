"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from bankApp.views import main_view, transfer_form_view, transfer_confirm_view, transfer_history_view, \
    transfer_sent_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),

    path('', main_view),
    path('transfer-form/', transfer_form_view, name='transfer-form'),
    path('transfer-confirm/', transfer_confirm_view, name='transfer-confirm'),
    path('transfer-sent/', transfer_sent_view, name='transfer-sent'),
    path('transfer-history/', transfer_history_view, name='transfer-history'),

]
