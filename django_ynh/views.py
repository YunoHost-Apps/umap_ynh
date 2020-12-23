import pprint

from django.http import HttpResponse
from django.shortcuts import redirect


def request_media_debug_view(request):
    """ debug request.META """
    if not request.user.is_authenticated:
        return redirect('admin:index')

    meta = pprint.pformat(request.META)
    html = f'<html><body>request.META: <pre>{meta}</pre></body></html>'

    return HttpResponse(html)
