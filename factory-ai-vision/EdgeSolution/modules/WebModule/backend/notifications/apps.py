"""
Notifications App
"""
import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)



class NotificationsConfig(AppConfig):
    """
    Notifications App Config
    """
    name = 'notifications'

    def ready(self):
        """
        Only load to data when runserver
        if ready run in migration will failed
        """
