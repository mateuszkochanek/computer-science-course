from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from bankApp.forms import TransferForm
from bankApp.models import Transfer


@login_required(login_url='login')
def main_view(request):
    context = {}
    return render(request, "index.html", context)


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
            transfer.save()
            transfer = Transfer.objects.filter(sender=user).order_by('-date').first()
            context = {'transfer': transfer}
            return render(request, "transfer/transfer-sent.html", context)
    form = TransferForm()
    context = {'form': form}
    return render(request, "transfer/transfer-form.html", context)

@login_required(login_url='login')
def transfer_history_view(request):
    user = request.user
    transfers = Transfer.objects.filter(sender=user).order_by('-date')
    context = {'transfers': transfers}
    return render(request, "transfer/transfer-history.html", context)
