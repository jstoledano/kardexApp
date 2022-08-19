from django.views.generic import ListView

from .models import Materia


class PortadaView(ListView):
    model = Materia
    template_name = "kardex/index.html"
