""" Admin UI Mixins """
from django.db import models
from ckeditor_widget.widgets import CKEditorWidget


class CKEditorAdminMixin:
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
