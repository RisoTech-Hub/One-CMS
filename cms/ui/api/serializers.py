from rest_framework import serializers

from ..models import Template, Theme


class TemplateSerializer(serializers.ModelSerializer[Template]):
    class Meta:
        model = Template
        fields = ["id", "name", "description", "content", "thumbnail", "icon"]


class TemplateNestedSerializer(serializers.ModelSerializer[Template]):
    class Meta:
        model = Template
        fields = ["id", "name", "description", "thumbnail", "icon"]


class ThemeSerializer(serializers.ModelSerializer[Theme]):
    templates = TemplateNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ["id", "name", "description", "thumbnail", "templates"]
