from django.shortcuts import render


def add_data_source(request):
    return render(request, 'app/add_data_source.html')


def add_user(request):
    return render(request, 'app/add_user.html')


def manage_store(request):
    return render(request, 'app/manage_store.html')


def sheet(request):
    return render(request, 'app/sheet.html')
