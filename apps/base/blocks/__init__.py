from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks

from .stream_form import (
    StreamFormCharFieldBlock,
    StreamFormCheckboxesFieldBlock,
    StreamFormCheckboxFieldBlock,
    StreamFormDateFieldBlock,
    StreamFormDateTimeFieldBlock,
    StreamFormDropdownFieldBlock,
    StreamFormFileFieldBlock,
    StreamFormImageFieldBlock,
    StreamFormNumberFieldBlock,
    StreamFormRadioButtonsFieldBlock,
    StreamFormStepBlock,
    StreamFormTextFieldBlock,
    StreamFormTimeFieldBlock,
)
from .html import (
    ButtonBlock,
    EmbedGoogleMapBlock,
    ImageBlock,
    ImageLinkBlock,
    DownloadBlock,
    EmbedVideoBlock,
    PageListBlock,
    PagePreviewBlock,
    QuoteBlock,
    RichTextBlock,
    TableBlock,
)
from .content import (  # noqa
    CardBlock,
    CarouselBlock,
    ContentWallBlock,
    ImageGalleryBlock,
    ModalBlock,
    NavDocumentLinkWithSubLinkBlock,
    NavExternalLinkWithSubLinkBlock,
    NavPageLinkWithSubLinkBlock,
    PriceListBlock,
    ReusableContentBlock,
)
from .layout import CardGridBlock, GridBlock, HeroBlock
from .base import (  # noqa
    BaseBlock,
    BaseLayoutBlock,
    BaseLinkBlock,
    ClassifierTermChooserBlock,
    AdvColumnSettings,
    AdvSettings,
    AdvTrackingSettings,
    CollectionChooserBlock,
)

# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    ("text", RichTextBlock(icon="cr-font")),
    ("button", ButtonBlock()),
    ("image", ImageBlock()),
    ("image_link", ImageLinkBlock()),
    (
        "html",
        blocks.RawHTMLBlock(
            icon="code",
            form_classname="monospace",
            label=_("HTML"),
        ),
    ),
    ("download", DownloadBlock()),
    ("embed_video", EmbedVideoBlock()),
    ("quote", QuoteBlock()),
    ("table", TableBlock()),
    ("google_map", EmbedGoogleMapBlock()),
    ("page_list", PageListBlock()),
    ("page_preview", PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ("card", CardBlock()),
    ("carousel", CarouselBlock()),
    ("image_gallery", ImageGalleryBlock()),
    ("modal", ModalBlock(HTML_STREAMBLOCKS)),
    ("pricelist", PriceListBlock()),
    ("reusable_content", ReusableContentBlock()),
]

NAVIGATION_STREAMBLOCKS = [
    ("page_link", NavPageLinkWithSubLinkBlock()),
    ("external_link", NavExternalLinkWithSubLinkBlock()),
    ("document_link", NavDocumentLinkWithSubLinkBlock()),
]

BASIC_LAYOUT_STREAMBLOCKS = [
    ("row", GridBlock(HTML_STREAMBLOCKS)),
    (
        "html",
        blocks.RawHTMLBlock(icon="code", form_classname="monospace", label=_("HTML")),
    ),
]

LAYOUT_STREAMBLOCKS = [
    (
        "hero",
        HeroBlock(
            [
                ("row", GridBlock(CONTENT_STREAMBLOCKS)),
                (
                    "cardgrid",
                    CardGridBlock(
                        [
                            ("card", CardBlock()),
                        ]
                    ),
                ),
                (
                    "html",
                    blocks.RawHTMLBlock(
                        icon="code", form_classname="monospace", label=_("HTML")
                    ),
                ),
            ]
        ),
    ),
    ("row", GridBlock(CONTENT_STREAMBLOCKS)),
    (
        "cardgrid",
        CardGridBlock(
            [
                ("card", CardBlock()),
            ]
        ),
    ),
    (
        "html",
        blocks.RawHTMLBlock(icon="code", form_classname="monospace", label=_("HTML")),
    ),
]

STREAMFORM_FIELDBLOCKS = [
    ("sf_singleline", StreamFormCharFieldBlock(group=_("Fields"))),
    ("sf_multiline", StreamFormTextFieldBlock(group=_("Fields"))),
    ("sf_number", StreamFormNumberFieldBlock(group=_("Fields"))),
    ("sf_checkboxes", StreamFormCheckboxesFieldBlock(group=_("Fields"))),
    ("sf_radios", StreamFormRadioButtonsFieldBlock(group=_("Fields"))),
    ("sf_dropdown", StreamFormDropdownFieldBlock(group=_("Fields"))),
    ("sf_checkbox", StreamFormCheckboxFieldBlock(group=_("Fields"))),
    ("sf_date", StreamFormDateFieldBlock(group=_("Fields"))),
    ("sf_time", StreamFormTimeFieldBlock(group=_("Fields"))),
    ("sf_datetime", StreamFormDateTimeFieldBlock(group=_("Fields"))),
    ("sf_image", StreamFormImageFieldBlock(group=_("Fields"))),
    ("sf_file", StreamFormFileFieldBlock(group=_("Fields"))),
]

STREAMFORM_BLOCKS = [
    ("step", StreamFormStepBlock(STREAMFORM_FIELDBLOCKS + HTML_STREAMBLOCKS)),
]
