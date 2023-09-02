from rest_framework import serializers

from ..models import Page as FlatPage


class FlatPageUpdateSerializer(serializers.ModelSerializer[FlatPage]):
    class Meta:
        model = FlatPage
        fields = ["content"]


class FlatPageCreateSerializer(serializers.ModelSerializer[FlatPage]):
    class Meta:
        model = FlatPage
        fields = ["url", "title", "template_name", "sites"]
