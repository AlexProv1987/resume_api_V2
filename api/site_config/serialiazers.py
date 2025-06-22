from rest_framework import serializers
from .models import PageWidget

class PageWidgetSerializer(serializers.ModelSerializer):
    widget_key = serializers.CharField(source='widget.key')
    widget_name = serializers.CharField(source='widget.name')

    class Meta:
        model = PageWidget
        fields = [
            'widget_key',
            'widget_name',
            'title_override',
            'display_order',
            'location',
            'is_visible',
        ]