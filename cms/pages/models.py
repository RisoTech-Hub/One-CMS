from django.contrib.flatpages.models import FlatPage
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta


class Page(ModelMeta, FlatPage):
    description = CharField(_("Description"), max_length=255, blank=True, null=True)
    keywords = CharField(_("Keywords"), max_length=1000, blank=True, null=True)

    _metadata = {
        "title": "title",
        "description": "description",
        "keywords": "keywords",
    }

    class Meta:
        verbose_name = _("CMS Page")
        verbose_name_plural = _("CMS Pages")
        db_table = "cms_page"
