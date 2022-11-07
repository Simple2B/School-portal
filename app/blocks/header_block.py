from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    StructBlock,
)


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
