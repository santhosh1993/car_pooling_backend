from django.urls import path, include
import SeatBooking.api_views

urlpatterns = [
    path('services/', SeatBooking.api_views.ServiceList.as_view(), name='Services'),
    path('userbooking/<int:id>/delete', SeatBooking.api_views.UserBookingDestroy.as_view(), name= 'Delete_Booking'),
    path('userbookingupdate/<str:type>/', SeatBooking.api_views.UserBookingUpdate.as_view()),
    path('userbooking/book', SeatBooking.api_views.UserBookingCreate.as_view(), name='Create_User_Booking'),
    path('services/create', SeatBooking.api_views.ServiceCreateAPI.as_view(),name='Services_Create')
]