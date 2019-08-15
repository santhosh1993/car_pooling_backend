from django.contrib import admin
from .models import UserBooking, ServiceType, Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'date_time', 'max_bookings', 'bookings_booked')
    fields = ['service_type', 'date_time', 'max_bookings']


admin.site.register(UserBooking)
admin.site.register(ServiceType)
admin.site.register(Service, ServiceAdmin)
