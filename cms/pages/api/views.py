from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from ..models import Page as FlatPage
from .serializers import FlatPageCreateSerializer, FlatPageUpdateSerializer


class FlatPageViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = FlatPageCreateSerializer
    queryset = FlatPage.objects.all()
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        self.serializer_class = FlatPageCreateSerializer
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = FlatPageUpdateSerializer
        return super().update(request, *args, **kwargs)
