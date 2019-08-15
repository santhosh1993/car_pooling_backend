from rest_framework import serializers
from .models import Service, UserBooking, ServiceType


class ServiceSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ('id', 'service', 'date_time', 'max_bookings', 'users')

    def get_users(self, instance):
        return UserBookingSerializer(instance.users(), many=True).data

    def get_service(self, instance):
        return ServiceTypeSerializer(instance.service_type).data

class UserBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooking
        fields = ('id', 'user_id')

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'type')
