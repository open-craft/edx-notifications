"""
Serializers (Django REST Framework) for Data Objects
"""

from rest_framework import serializers

from notifications.base_data import (
    DictField
)

from notifications.data import (
    NotificationMessage,
    NotificationType
)


class DictFieldSerializer(serializers.WritableField):
    """
    A specialized serializer for a dictionary field
    """

    def to_native(self, obj):
        """
        to json format
        """
        return DictField.to_json(obj)

    def from_native(self, data):
        """
        from json format
        """
        obj = DictField.from_json(data)
        return obj


class NotificationTypeSerializer(serializers.Serializer):
    """
    DRF Serializer definition for NotificationType
    """

    name = serializers.CharField(max_length=256)

    def restore_object(self, attrs, instance=None):
        """
        Instantiate a new object from the deserialized data
        """

        if instance is not None:
            raise NotImplementedError()

        return NotificationType(**attrs)  # pylint: disable=star-args


class NotificationMessageSerializer(serializers.Serializer):
    """
    DRF Serializer definition for NotificationMessage
    """

    id = serializers.IntegerField()
    msg_type = NotificationTypeSerializer()
    namespace = serializers.CharField(max_length=128, required=False)
    from_user_id = serializers.IntegerField(required=False)
    payload = DictFieldSerializer()
    deliver_no_earlier_than = serializers.DateTimeField(required=False)
    expires_at = serializers.DateTimeField(required=False)
    expires_secs_after_read = serializers.IntegerField(required=False)
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()

    def restore_object(self, attrs, instance=None):
        """
        Instantiate a new object from the deserialized data
        """

        if instance is not None:
            raise NotImplementedError()

        msg = NotificationMessage(**attrs)  # pylint: disable=star-args
        return msg
