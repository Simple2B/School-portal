from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page, get_page_models
from apps.base.forms import SearchForm
from apps.base.models import GeneralSettings
from apps.base.templatetags.cms_tags import get_name_of_class


def search(request):
    """
    Searches pages across the entire site.
    """
    search_form = SearchForm(request.GET)
    pagetypes = []
    results = None
    results_paginated = None

    if search_form.is_valid():
        search_query = search_form.cleaned_data["s"]
        search_model = search_form.cleaned_data["t"]

        # get all page models
        pagemodels = sorted(get_page_models(), key=get_name_of_class)
        # filter based on is search_filterable
        for model in pagemodels:
            if hasattr(model, "search_filterable") and model.search_filterable:
                pagetypes.append(model)

        results = Page.objects.live()
        if search_model:
            try:
                # If provided a model name, try to get it
                model = ContentType.objects.get(model=search_model).model_class()
                results = results.type(model)
            except ContentType.DoesNotExist:
                # Maintain existing behavior of only returning objects if the page type is real
                results = None

        # get and paginate results
        if results:
            results = results.search(search_query)
            paginator = Paginator(
                results, GeneralSettings.for_request(request).search_num_results
            )
            page = request.GET.get("p", 1)
            try:
                results_paginated = paginator.page(page)
            except PageNotAnInteger:
                results_paginated = paginator.page(1)
            except EmptyPage:
                results_paginated = paginator.page(1)
            except InvalidPage:
                results_paginated = paginator.page(1)

    # Render template
    return render(
        request,
        "search/search.html",
        {
            "request": request,
            "pagetypes": pagetypes,
            "form": search_form,
            "results": results,
            "results_paginated": results_paginated,
        },
    )
