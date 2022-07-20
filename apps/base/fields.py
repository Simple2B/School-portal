from django.db import models
from django.forms.widgets import Textarea

from apps.base.widgets import ColorPickerWidget


class ColorField(models.CharField):
    """
    A CharField which uses the HTML5 color picker widget.
    """

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 255
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs["widget"] = ColorPickerWidget
        return super().formfield(**kwargs)


class MonospaceField(models.TextField):
    """
    A TextField which renders as a large HTML textarea with monospace font.
    """

    def formfield(self, **kwargs):
        kwargs["widget"] = Textarea(
            attrs={
                "rows": 12,
                "class": "monospace",
                "spellcheck": "false",
            }
        )
        return super().formfield(**kwargs)
