from django.shortcuts import render
from django.utils.translation import ugettext as _


def handler403(request):
    print(request)
    return render(request, 'error.html', {
        'error': '403',
        'title': _('Access Denied')
    })


def handler404(request):
    return render(request, 'error.html', {
        'error': '404',
        'title': _('Not Found')
    })


def handler500(request):
    return render(request, 'error.html', {
        'error': '500',
        'title': _('Server Error')
    })
