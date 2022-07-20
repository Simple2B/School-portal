from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from apps.search import views as search_views
from apps.base.settings import crx_settings
from apps.base.views import favicon, robots, serve_protected_file

urlpatterns = [
    # Admin
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    # Documents
    path("documents/", include(wagtaildocs_urls)),
    # Search
    path("search/", search_views.search, name="search"),
    # Sitemap
    path("sitemap.xml", sitemap),
    path(r"favicon.ico", favicon, name="codered_favicon"),
    path(r"robots.txt", robots, name="codered_robots"),
    path(r"sitemap.xml", sitemap, name="codered_sitemap"),
    re_path(
        r"^{0}(?P<path>.*)$".format(crx_settings.CRX_PROTECTED_MEDIA_URL.lstrip("/")),
        serve_protected_file,
        name="serve_protected_file",
    ),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
