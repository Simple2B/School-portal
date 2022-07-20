from django.utils.translation import gettext_lazy as _
from django import forms

from wagtail.core import blocks

from base.wagtail_flexible_forms import blocks as form_blocks
from base.blocks.base import BaseBlock, AdvSettings
from base.forms import SecureFileField


class FormAdvSettings(AdvSettings):

    condition_trigger_id = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Condition Trigger ID"),
        help_text=_(
            'The "Custom ID" of another field that that will trigger this field to be shown/hidden.'
        ),  # noqa
    )
    condition_trigger_value = blocks.CharBlock(
        required=False,
        max_length=255,
        label=_("Condition Trigger Value"),
        help_text=_(
            'The value of the field in "Condition Trigger ID" that will trigger this field to be shown.'
        ),  # noqa
    )


class FormBlockMixin(BaseBlock):
    class Meta:
        abstract = True

    advsettings_class = FormAdvSettings


class StreamFormFieldBlock(form_blocks.OptionalFormFieldBlock, FormBlockMixin):
    pass


class StreamFormCharFieldBlock(form_blocks.CharFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Text or Email input")
        icon = "cr-window-minimize"


class StreamFormTextFieldBlock(form_blocks.TextFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Multi-line text")
        icon = "cr-align-left"


class StreamFormNumberFieldBlock(form_blocks.NumberFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Numbers only")
        icon = "cr-hashtag"


class StreamFormCheckboxFieldBlock(form_blocks.CheckboxFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Single Checkbox")
        icon = "cr-check-square-o"


class StreamFormRadioButtonsFieldBlock(
    form_blocks.RadioButtonsFieldBlock, FormBlockMixin
):
    class Meta:
        label = _("Radios")
        icon = "list-ul"


class StreamFormDropdownFieldBlock(form_blocks.DropdownFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Dropdown")
        icon = "cr-list-alt"


class StreamFormCheckboxesFieldBlock(form_blocks.CheckboxesFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Checkboxes")
        icon = "list-ul"


class StreamFormDateFieldBlock(form_blocks.DateFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Date")
        icon = "date"

    field_class = blocks.DateField
    widget = forms.DateInput


class StreamFormTimeFieldBlock(form_blocks.TimeFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Time")
        icon = "time"

    field_class = forms.TimeField
    widget = forms.TimeInput


class StreamFormDateTimeFieldBlock(form_blocks.DateTimeFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Date and Time")
        icon = "date"

    field_class = forms.DateTimeField
    widget = forms.DateTimeInput


class StreamFormImageFieldBlock(form_blocks.ImageFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Image Upload")
        icon = "image"


class StreamFormFileFieldBlock(form_blocks.FileFieldBlock, FormBlockMixin):
    class Meta:
        label = _("Secure File Upload")
        icon = "upload"

    field_class = SecureFileField


class StreamFormStepBlock(form_blocks.FormStepBlock):
    form_fields = blocks.StreamBlock()

    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(
            local_blocks=[("form_fields", blocks.StreamBlock(local_blocks))]
        )
