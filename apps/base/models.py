from django.db import models
from django.utils.translation import gettext_lazy as _


from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.core.blocks import RichTextBlock, CharBlock
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.models import register_snippet
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images import get_image_model_string
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    HelpPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)


@register_snippet
class Carousel(ClusterableModel):
    """
    Model that represents a Carousel. Can be modified through the snippets UI.
    Selected through Page StreamField bodies by the CarouselSnippetChooser in
    snippet_choosers.py
    """

    class Meta:
        verbose_name = _("Carousel")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    show_controls = models.BooleanField(
        default=True,
        verbose_name=_("Show controls"),
        help_text=_(
            "Shows arrows on the left and right of the carousel to advance next or previous slides."
        ),  # noqa
    )
    show_indicators = models.BooleanField(
        default=True,
        verbose_name=_("Show indicators"),
        help_text=_(
            "Shows small indicators at the bottom of the carousel based on the number of slides."
        ),  # noqa
    )
    animation = models.CharField(
        blank=True,
        max_length=20,
        choices=None,
        default="",
        verbose_name=_("Animation"),
        help_text=_("The animation when transitioning between slides."),
    )

    panels = [
        MultiFieldPanel(
            heading=_("Slider"),
            children=[
                FieldPanel("name"),
                FieldPanel("show_controls"),
                FieldPanel("show_indicators"),
                FieldPanel("animation"),
            ],
        ),
        InlinePanel("carousel_slides", label=_("Slides")),
    ]

    def __str__(self):
        return self.name


class CarouselSlide(Orderable, models.Model):
    """
    Represents a slide for the Carousel model. Can be modified through the
    snippets UI.
    """

    class Meta(Orderable.Meta):
        verbose_name = _("Carousel Slide")

    carousel = ParentalKey(
        Carousel,
        related_name="carousel_slides",
        verbose_name=_("Carousel"),
    )
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Image"),
    )
    background_color = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Background color"),
        help_text=_("Hexadecimal, rgba, or CSS color notation (e.g. #ff0011)"),
    )
    custom_css_class = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom CSS class"),
    )
    custom_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom ID"),
    )

    content = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
            "video": {"max_num": 5},
        },
        use_json_field=True,
        null=True,
        blank=True,
    )

    panels = [
        ImageChooserPanel("image"),
        FieldPanel("background_color"),
        FieldPanel("custom_css_class"),
        FieldPanel("custom_id"),
        StreamFieldPanel("content"),
    ]


@register_snippet
class Classifier(ClusterableModel):
    """
    Simple and generic model to organize/categorize/group pages.
    """

    class Meta:
        verbose_name = _("Classifier")
        verbose_name_plural = _("Classifiers")
        ordering = ["name"]

    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        verbose_name=_("Slug"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    panels = [FieldPanel("name"), InlinePanel("terms", label=_("Classifier Terms"))]

    def __str__(self):
        return self.name


class ClassifierTerm(Orderable, models.Model):
    """
    Term used to categorize a page.
    """

    class Meta(Orderable.Meta):
        verbose_name = _("Classifier Term")
        verbose_name_plural = _("Classifier Terms")

    classifier = ParentalKey(
        Classifier,
        related_name="terms",
        verbose_name=_("Classifier"),
    )
    slug = models.SlugField(
        allow_unicode=True,
        unique=True,
        verbose_name=_("Slug"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return "{0} > {1}".format(self.classifier.name, self.name)


@register_snippet
class Navbar(models.Model):
    """
    Snippet for site navigation bars (header, main menu, etc.)
    """

    class Meta:
        verbose_name = _("Navigation Bar")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    custom_css_class = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom CSS Class"),
    )
    custom_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom ID"),
    )

    panels = [
        FieldPanel("name"),
        MultiFieldPanel(
            [
                FieldPanel("custom_css_class"),
                FieldPanel("custom_id"),
            ],
            heading=_("Attributes"),
        ),
    ]

    def __str__(self):
        return self.name


@register_snippet
class Footer(models.Model):
    """
    Snippet for website footer content.
    """

    class Meta:
        verbose_name = _("Footer")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    custom_css_class = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom CSS Class"),
    )
    custom_id = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Custom ID"),
    )

    panels = [
        FieldPanel("name"),
        MultiFieldPanel(
            [
                FieldPanel("custom_css_class"),
                FieldPanel("custom_id"),
            ],
            heading=_("Attributes"),
        ),
    ]

    def __str__(self):
        return self.name


@register_snippet
class ReusableContent(models.Model):
    """
    Snippet for resusable content in streamfields.
    """

    class Meta:
        verbose_name = _("Reusable Content")
        verbose_name_plural = _("Reusable Content")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )

    panels = [FieldPanel("name")]

    def __str__(self):
        return self.name


@register_snippet
class ContentWall(models.Model):
    """
    Snippet that restricts access to a page with a modal.
    """

    class Meta:
        verbose_name = _("Content Wall")

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    is_dismissible = models.BooleanField(
        default=True,
        verbose_name=_("Dismissible"),
    )
    show_once = models.BooleanField(
        default=True,
        verbose_name=_("Show once"),
        help_text=_(
            "Do not show the content wall to the same user again after it has been closed."
        ),
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("is_dismissible"),
                FieldPanel("show_once"),
            ],
            heading=_("Content Wall"),
        ),
    ]

    def __str__(self):
        return self.name


@register_setting(icon="cr-desktop")
class LayoutSettings(ClusterableModel, BaseSetting):
    class Meta:
        verbose_name = _("Layout")

    logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Logo"),
        help_text=_("Brand logo used in the navbar and throughout the site"),
    )
    favicon = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="favicon",
        verbose_name=_("Favicon"),
    )
    navbar_color_scheme = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Navbar color scheme"),
        help_text=_(
            "Optimizes text and other navbar elements for use with light or dark backgrounds."
        ),  # noqa
    )
    navbar_class = models.CharField(
        blank=True,
        max_length=255,
        default="",
        verbose_name=_("Navbar CSS class"),
        help_text=_(
            'Custom classes applied to navbar e.g. "bg-light", "bg-dark", "bg-primary".'
        ),
    )
    navbar_fixed = models.BooleanField(
        default=False,
        verbose_name=_("Fixed navbar"),
        help_text=_("Fixed navbar will remain at the top of the page when scrolling."),
    )
    navbar_wrapper_fluid = models.BooleanField(
        default=True,
        verbose_name=_("Full width navbar"),
        help_text=_("The navbar will fill edge to edge."),
    )
    navbar_content_fluid = models.BooleanField(
        default=False,
        verbose_name=_("Full width navbar contents"),
        help_text=_("Content within the navbar will fill edge to edge."),
    )
    navbar_collapse_mode = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Collapse navbar menu"),
        help_text=_(
            "Control on what screen sizes to show and collapse the navbar menu links."
        ),
    )
    navbar_format = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Navbar format"),
    )
    navbar_search = models.BooleanField(
        default=True,
        verbose_name=_("Search box"),
        help_text=_("Show search box in navbar"),
    )
    frontend_theme = models.CharField(
        blank=True,
        max_length=50,
        choices=None,
        default="",
        verbose_name=_("Theme variant"),
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("logo"),
                ImageChooserPanel("favicon"),
            ],
            heading=_("Branding"),
        ),
        InlinePanel(
            "site_navbar",
            help_text=_("Choose one or more navbars for your site."),
            heading=_("Site Navbars"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("navbar_color_scheme"),
                FieldPanel("navbar_class"),
                FieldPanel("navbar_fixed"),
                FieldPanel("navbar_wrapper_fluid"),
                FieldPanel("navbar_content_fluid"),
                FieldPanel("navbar_collapse_mode"),
                FieldPanel("navbar_format"),
                FieldPanel("navbar_search"),
            ],
            heading=_("Site Navbar Layout"),
        ),
        InlinePanel(
            "site_footer",
            help_text=_("Choose one or more footers for your site."),
            heading=_("Site Footers"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("frontend_theme"),
            ],
            heading=_("Theming"),
        ),
    ]


class NavbarOrderable(Orderable, models.Model):
    navbar_chooser = ParentalKey(
        LayoutSettings, related_name="site_navbar", verbose_name=_("Site Navbars")
    )
    navbar = models.ForeignKey(
        Navbar,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    panels = [SnippetChooserPanel("navbar")]


class FooterOrderable(Orderable, models.Model):
    footer_chooser = ParentalKey(
        LayoutSettings, related_name="site_footer", verbose_name=_("Site Footers")
    )
    footer = models.ForeignKey(
        Footer,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    panels = [SnippetChooserPanel("footer")]


@register_setting(icon="cr-google")
class AnalyticsSettings(BaseSetting):
    """
    Tracking and Google Analytics.
    """

    class Meta:
        verbose_name = _("Tracking")

    ga_tracking_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("UA Tracking ID"),
        help_text=_(
            'Your Google "Universal Analytics" tracking ID (begins with "UA-")'
        ),
    )
    ga_g_tracking_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("G Tracking ID"),
        help_text=_('Your Google Analytics 4 tracking ID (begins with "G-")'),
    )
    ga_track_button_clicks = models.BooleanField(
        default=False,
        verbose_name=_("Track button clicks"),
        help_text=_(
            "Track all button clicks using Google Analytics event tracking. Event tracking details can be specified in each button’s advanced settings options."
        ),  # noqa
    )
    gtm_id = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Google Tag Manager ID"),
        help_text=_('Begins with "GTM-"'),
    )

    panels = [
        HelpPanel(
            heading=_("Know your tracking"),
            content=_(
                "<h3><b>Which tracking IDs do I need?</b></h3>"
                "<p>Before adding tracking to your site, "
                '<a href="https://docs.coderedcorp.com/wagtail-crx/how_to/add_tracking_scripts.html" '  # noqa
                'target="_blank">read about the difference between UA, G, GTM, '
                "and other tracking IDs</a>.</p>"
            ),
        ),
        MultiFieldPanel(
            [
                FieldPanel("ga_tracking_id"),
                FieldPanel("ga_g_tracking_id"),
                FieldPanel("ga_track_button_clicks"),
            ],
            heading=_("Google Analytics"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("gtm_id"),
            ],
            heading=_("Google Tag Manager"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("head_scripts"),
                FieldPanel("body_scripts"),
            ],
            heading=_("Other Tracking Scripts"),
        ),
    ]


@register_setting(icon="cr-universal-access")
class ADASettings(BaseSetting):
    """
    Accessibility related options.
    """

    class Meta:
        verbose_name = "Accessibility"

    skip_navigation = models.BooleanField(
        default=False,
        verbose_name=_("Show skip navigation link"),
        help_text=_(
            'Shows a "Skip Navigation" link above the navbar that takes you directly to the main content.'
        ),  # noqa
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("skip_navigation"),
            ],
            heading=_("Accessibility"),
        )
    ]


@register_setting(icon="cog")
class GeneralSettings(BaseSetting):

    from_email_address = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("From email address"),
        help_text=_(
            'The default email address this site appears to send from. For example: "sender@example.com" or "Sender Name <sender@example.com>" (without quotes)'
        ),  # noqa
    )
    search_num_results = models.PositiveIntegerField(
        default=10,
        verbose_name=_("Number of results per page"),
    )
    external_new_tab = models.BooleanField(
        default=False, verbose_name=_("Open all external links in new tab")
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("from_email_address"),
            ],
            _("Email"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("search_num_results"),
            ],
            _("Search Settings"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("external_new_tab"),
            ],
            _("Links"),
        ),
    ]

    class Meta:
        verbose_name = _("General")


@register_setting(icon="cr-puzzle-piece")
class GoogleApiSettings(BaseSetting):
    """
    Settings for Google API services.
    """

    class Meta:
        verbose_name = _("Google API")

    google_maps_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Google Maps API Key"),
        help_text=_("The API Key used for Google Maps."),
    )


class HomePage(Page):
    body = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
            "video": {"max_num": 5},
        },
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [FieldPanel("body")]


class StandardIndexPage(Page):
    heading = RichTextField(
        null=False,
        blank=False,
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overview_text = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
            "video": {"max_num": 5},
        },
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("banner_image"),
        FieldPanel("overview_text"),
    ]


class StandardPage(Page):
    heading = RichTextField(
        null=False,
        blank=False,
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    overview_text = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("video", EmbedBlock()),
        ],
        block_counts={
            "heading": {"min_num": 1},
            "image": {"max_num": 5},
            "video": {"max_num": 5},
        },
        use_json_field=True,
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("heading"),
        FieldPanel("banner_image"),
        FieldPanel("overview_text"),
    ]
