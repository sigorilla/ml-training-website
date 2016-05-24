from ml_training.settings import TITLE, DESCRIPTION, FILTER_KEY


def current_uri(request):
    return {
        'current_uri': request.build_absolute_uri(),
        'current_host': request.get_host(),
        'request': request
    }


def constants(request):
    return {
        'TITLE': TITLE,
        'DESCRIPTION': DESCRIPTION,
        'FILTER_KEY': FILTER_KEY
    }
