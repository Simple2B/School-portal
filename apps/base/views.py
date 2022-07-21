import mimetypes
import os
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from apps.base.models import LayoutSettings
from apps.base.settings import crx_settings


@login_required
def serve_protected_file(request, path):
    """
    Function that serves protected files uploaded from forms.
    """
    # Fully resolve all provided paths.
    mediapath = os.path.abspath(crx_settings.CRX_PROTECTED_MEDIA_ROOT)
    fullpath = os.path.abspath(os.path.join(mediapath, path))

    # Path must be a sub-path of the PROTECTED_MEDIA_ROOT, and exist.
    if fullpath.startswith(mediapath) and os.path.isfile(fullpath):
        mimetype, encoding = mimetypes.guess_type(fullpath)
        with open(fullpath, "rb") as f:
            response = HttpResponse(f.read(), content_type=mimetype)
        if encoding:
            response["Content-Encoding"] = encoding

        return response
    raise Http404()


def favicon(request):
    icon = LayoutSettings.for_request(request).favicon
    if icon:
        return HttpResponsePermanentRedirect(icon.get_rendition("original").url)
    raise Http404()


def robots(request):
    return render(request, "robots.txt", content_type="text/plain")
