from wagtail.models import Page
from app.models.info_page import InfoPage


class NewsItemsPage(Page):
    def get_context(self, request):
        news = InfoPage.objects.filter(type="news")
        context = super().get_context(request)
        context["news"] = news
        return context
