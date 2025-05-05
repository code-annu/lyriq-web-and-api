from rest_framework import serializers

class SizeSerializer(serializers.Serializer):
    size = serializers.IntegerField(
        min_value=1,
        required=True,
        error_messages={
            'invalid': 'Size must be an integer.',
            'min_value': 'Size must be at least 1.'
        }
    )