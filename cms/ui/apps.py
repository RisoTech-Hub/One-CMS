from django.apps import AppConfig


class CmsUIConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cms.ui"
    verbose_name = "CMS"

    def ready(self):
        try:
            import cms.ui.signals  # noqa F401
        except ImportError:
            pass
