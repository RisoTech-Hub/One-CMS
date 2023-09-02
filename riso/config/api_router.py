from cms.pages.api.views import FlatPageViewSet
from cms.ui.api.views import TemplateAPIView, ThemeAPIView
from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from riso.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("pages", FlatPageViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("themes/", ThemeAPIView.as_view(), name="themes"),
    path("templates/<int:pk>/", TemplateAPIView.as_view(), name="templates"),
]
