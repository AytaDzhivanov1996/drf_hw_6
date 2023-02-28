from rest_framework import serializers


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'youtube.com' not in value.get('link_video'):
            raise serializers.ValidationError('Ссылка должна быть только на YouTube')
