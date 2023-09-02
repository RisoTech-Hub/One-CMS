from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.flatpages.models import FlatPage

from .models import Page

admin.site.unregister(FlatPage)


@admin.register(Page)
class PageAdmin(ModelAdmin):
    pass
