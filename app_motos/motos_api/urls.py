
from django.urls import path
from .views import MotoListApiView

urlpatterns=[
    path('', MotoListApiView.as_view(), name="Moto_list")
]