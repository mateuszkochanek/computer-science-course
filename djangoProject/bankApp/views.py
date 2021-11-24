from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
# Create your views here.
from django.utils import timezone
from django.views.generic import UpdateView
from django_rest.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from bankApp.forms import TransferForm, ReceiverForm
from bankApp.models import Transfer
from bankApp.serializers import UserSerializer, TransfersHistorySerializer, TransferSendSerializer, LoginSerializer


@login_required(login_url='login')
def main_view(request):
    context = {}
    return render(request, "index.html", context)


@login_required(login_url='login')
def transfers_verification_view(request):
    transfers = Transfer.objects.filter().order_by('-date')
    context = {'transfers': transfers}
    return render(request, "admin/verification-of-transfers.html", context)


@login_required(login_url='login')
def transfers_verification(request, id):
    if request.user.is_staff:
        transfer = Transfer.objects.get(id=id)
        transfer.is_confirmed = True
        transfer.save()
    return redirect('/admin/transfer-verification/')


@login_required(login_url='login')
def transfer_form_view(request):
    form = TransferForm()
    context = {'form': form}
    return render(request, "transfer/transfer-form.html", context)


@login_required(login_url='login')
def transfer_confirm_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        form.disable_form_fields()
        context = {'form': form}
        return render(request, "transfer/transfer-confirm.html", context)
    else:
        form = TransferForm()
        context = {'form': form}
        return render(request, "transfer/transfer-form.html", context)


@login_required(login_url='login')
def transfer_sent_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            user = request.user
            transfer = form.save(commit=False)
            transfer.sender = user
            with connection.cursor() as cursor:
                query = 'INSERT INTO bankApp_transfer (sender_id, recipient_name, recipient_account, date, title, amount, is_confirmed) VALUES ("' + str(
                    transfer.sender.id) + '", "' + transfer.recipient_name + '", "' + transfer.recipient_account + '", "' + str(
                    timezone.now()) + '", "' + transfer.title + '","' + str(transfer.amount) + '",FALSE)'
                cursor.execute(query)
                query = "SELECT * FROM bankApp_transfer WHERE sender_id = '%s' ORDER BY date DESC LIMIT 1"
                cursor.execute(query, [transfer.sender.id])
                dictionary = dictfetchall(cursor)
                transfer = Transfer(**dictionary[0])
            context = {'transfer': transfer}
            return render(request, "transfer/transfer-sent.html", context)
    form = TransferForm()
    context = {'form': form}
    return render(request, "transfer/transfer-form.html", context)


@login_required(login_url='login')
def transfer_history_view(request):
    user = request.user
    transfers = []
    if request.method == 'POST':
        form = ReceiverForm(request.POST)
        transfer = form.save(commit=False)
        receiver_name = transfer.recipient_name
        with connection.cursor() as cursor:
            query = 'SELECT * FROM bankApp_transfer WHERE recipient_name = "' + transfer.recipient_name + '" AND sender_id = "' + str(
                request.user.id) + '"  ORDER BY date DESC'
            cursor.execute(query)
            dictionary = dictfetchall(cursor)
        for transfer in dictionary:
            transfers.append(Transfer(**transfer))
    else:
        form = ReceiverForm()
        transfers = Transfer.objects.filter(sender=user).order_by('-date')
    context = {'transfers': transfers, 'form': form}
    return render(request, "transfer/transfer-history.html", context)


@api_view(['POST'])
@permission_classes((AllowAny,))
def user_registration_api(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def user_login_api(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     login(request, user)
#     return JsonResponse(UserSerializer(user).data, status=400)
#
# @api_view(['POST'])
# @permission_classes((AllowAny,))
# def user_logout_api(self, request):
#     logout(request)
#     return JsonResponse({"logout": "Successful"}, status=400)


@api_view(['GET'])
@authentication_classes((JWTAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def transfers_history_api(request):
    if request.method == 'GET':
        transfers = []
        for item in Transfer.objects.all():
            if item.sender_id == request.user.id:
                transfers.append(item)

        serializer = TransfersHistorySerializer(transfers, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes((JWTAuthentication, SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated, ))
def transfer_send_api(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransferSendSerializer(data=data)
        if serializer.is_valid():
            print(request.user)
            serializer.save(sender=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
