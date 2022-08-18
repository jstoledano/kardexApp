from django.contrib import admin
from django.urls import path
from kardex.views import PortadaView

urlpatterns = [
    path('', PortadaView.as_view(), name='portada'),
    path('admin/', admin.site.urls),
]
