from django.urls import path, include
import User.api_views

urlpatterns = [
   path('login/', User.api_views.login, name='login'),
]