"""
Serializers
"""

import logging

from rest_framework import serializers

from ..models import Notification

logger = logging.getLogger(__name__)


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    """NotificationSerializer"""

    class Meta:
        model = Notification
        fields = ["id", "title", "details"]
