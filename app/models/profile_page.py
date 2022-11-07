from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from app.blocks.base_stream_block import BaseStreamBlock
from app.models.profile import Profile


class ProfilePage(Page):
    def get_context(self, request):
        profile = Profile.objects.get(pk=request.user.pk)
        context = super().get_context(request)
        context['profile'] = profile
        return context
    
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True, use_json_field=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]
