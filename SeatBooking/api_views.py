from .models import Service, UserBooking, ServiceType
from .serializers import ServiceSerializer, UserBookingSerializer

from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.utils.timezone import make_aware

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class ServiceList(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class UserBookingDestroy(DestroyAPIView):
    queryset = UserBooking.objects.all()
    serializer_class = UserBookingSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kargs):
        booking_id = request.data.get('id')
        response = super().delete(request, *args, **kargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete(f'userbooking_data_{booking_id}')

        return response

class UserBookingUpdate(APIView):
    def post(self, request, type, format=None):
        ids = request.data.get('ids')
        print(type)
        for id in ids:
            userbooking = UserBooking.objects.filter(id=id)
            if userbooking.exists():
                userbooking = userbooking.get()
                if type == 'turned_up':
                    userbooking.turned_up_status = 't'
                    userbooking.save()
                else:
                    userbooking.delete()

                from django.core.cache import cache
                cache.delete(f'userbooking_data_{userbooking.id}')

            else:
                return Response({"message": "Invalid user booking"}, HTTP_400_BAD_REQUEST)

        return Response({"message": "Status got updated"}, HTTP_200_OK)

class UserBookingCreate(APIView):
    def post(self, request, format=None):
        service_id = request.data.get('service_id')
        user_id = request.data.get('user_id')
        service = Service.objects.filter(id=service_id)
        user_booking = UserBooking.objects.filter(id=user_id)
        if service.exists():
            if user_booking.exists():
                return Response({"message": "Sorry there is already a booking"}, HTTP_200_OK)
            else:
                user_booking = UserBooking()
                user_booking.service = service.get()
                user_booking.user_id = user_id
                user_booking.save()
                return Response({"message": "User Booking created"}, HTTP_200_OK)

        else:
            return Response({"message": "Invalid service"}, HTTP_400_BAD_REQUEST)


class ServiceCreateAPI(APIView):
    def post(self, request, format=None):
        service_type_id = request.data.get('service_type_id')
        service_data = request.data.get('service_data')
        service_type = ServiceType.objects.filter(id=service_type_id)

        if service_type.exists():
            service_type = service_type.get()
            for each in service_data:
                date_time = each['date_time']
                date_time = make_aware(datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S'))
                max_bookings = each['max_bookings']
                service = Service.objects.filter(date_time=date_time, service_type=service_type)
                if service.exists():
                    service = service.get()
                else:
                    service = Service()

                service.date_time = date_time
                service.max_bookings = max_bookings
                service.service_type = service_type
                service.save()

            return Response({"message": "New services are created/updated"}, HTTP_200_OK)

        return Response({"message": "Invalid service type"}, HTTP_400_BAD_REQUEST)

class ServiceTypeCreateAPI(APIView):
    def post(self, request, format=None):
        type = request.data.get('type')
        service_type = ServiceType.objects.filter(type=type)

        if service_type.exists():
            return Response({"message": "Service Type already exists"}, HTTP_200_OK)
        else:
            service_type = ServiceType()
            service_type.type = type
            service_type.save()
            return Response({"message": 'New service is created'}, HTTP_200_OK)
