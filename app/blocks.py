from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        template = "blocks/image_block.html"


class HeaderBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        template = "blocks/header_block.html"


class BaseStreamBlock(StreamBlock):
    heading_block = HeaderBlock()
    paragraph_block = RichTextBlock(
        template="blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        template="blocks/embed_block.html"
    )
