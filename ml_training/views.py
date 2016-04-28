# -*- coding: utf-8 -*-
from django.shortcuts import render


def handler403(request):
    return render(request, 'error.html', {
        'error': '403',
        'title': 'Запрещено'
    })


def handler404(request):
    return render(request, 'error.html', {
        'error': '404',
        'title': 'Не найдено'
    })


def handler500(request):
    return render(request, 'error.html', {
        'error': '500',
        'title': 'Ошибка сервера'
    })
