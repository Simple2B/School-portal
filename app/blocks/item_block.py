from wagtail.blocks import (
    CharBlock,
    StructBlock,
)


class ItemBlock(StructBlock):
    heading_text = CharBlock()

    class Meta:
        template = "blocks/item_block.html"
