from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import (
    CharBlock,
    StructBlock,
)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        template = "blocks/image_block.html"
