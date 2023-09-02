from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from ..models import Template, Theme
from .serializers import TemplateSerializer, ThemeSerializer


class ThemeAPIView(ListAPIView):
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
    permission_classes = [IsAdminUser]


class TemplateAPIView(RetrieveAPIView):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    permission_classes = [IsAdminUser]
