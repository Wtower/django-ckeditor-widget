django-ckeditor-widget
======================

A CKEditor widget for Django that includes an admin mixin.

How to use
----------

Install using pip::

    pip install django-ckeditor-widget


Then use as any other widget::

    from django import forms
    from ckeditor_widget.widgets import CKEditorWidget

    class MyForm(forms.Form):
        body = forms.TextField(widget=CKEditorWidget)

https://docs.djangoproject.com/en/1.11/ref/forms/widgets/#specifying-widgets

Make sure that CKEditor is provided in static files as ``ckeditor/ckeditor.js``.

Admin
-----

The app conveniently provides an admin mixin that uses CKEditor for all text fields.
Simply inherit from the mixin::

    from django.contrib import admin
    from ckeditor_widget.admin import CKEditorAdminMixin
    from myapp import models

    @admin.register(models.Product)
    class ProductAdmin(CKEditorAdminMixin, admin.ModelAdmin):
        pass

Akternatively, specify ``formfield_overrides``::

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
