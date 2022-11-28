from wagtail.embeds.blocks import EmbedBlock
from wagtail.blocks import RichTextBlock, StreamBlock

from app.blocks.header_block import HeaderBlock
from app.blocks.image_block import ImageBlock
from app.blocks.item_block import ItemBlock


class BaseStreamBlock(StreamBlock):
    heading_block = HeaderBlock()
    paragraph_block = RichTextBlock(template="blocks/paragraph_block.html")
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        template="blocks/embed_block.html", max_width=600, max_height=338
    )
    item_block = ItemBlock()
