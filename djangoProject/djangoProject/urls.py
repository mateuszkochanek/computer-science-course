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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from bankApp.views import main_view, transfer_form_view, transfer_confirm_view, transfer_history_view, \
    transfer_sent_view, transfers_verification_view, transfers_verification, user_registration_api, transfer_send_api, \
    transfers_history_api#, user_login_api, user_logout_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),

    path('admin/transfer-verification/', transfers_verification_view, name='verification-of-transfers'),
    path('admin/transfer-verification/<int:id>/', transfers_verification),

    path('', main_view),
    path('transfer-form/', transfer_form_view, name='transfer-form'),
    path('transfer-confirm/', transfer_confirm_view, name='transfer-confirm'),
    path('transfer-sent/', transfer_sent_view, name='transfer-sent'),
    path('transfer-history/', transfer_history_view, name='transfer-history'),

    path('api/user_registration/', user_registration_api, name='api_user_registration'),
    #path('api/login/', user_login_api, name='api_user_login'),
    #path('api/logout/', user_logout_api, name='api_user_logout'),
    path('api/transfer_send/', transfer_send_api, name='api_transfer_confirmed'),
    path('api/transfers_history/', transfers_history_api, name='api_transfers_history'),

    url('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
