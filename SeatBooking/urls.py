from django.urls import path, include
import SeatBooking.api_views

urlpatterns = [
   path('services/', SeatBooking.api_views.ServiceList.as_view(),name='Services'),
]