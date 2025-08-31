from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_repr = serializers.CharField(source='target', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_repr', 'is_read', 'timestamp']
