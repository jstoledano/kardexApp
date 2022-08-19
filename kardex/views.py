from django.views.generic import ListView

from .models import Materia


class PortadaView(ListView):
    queryset = Materia.objects.all().order_by('semestre', 'clave')
    template_name = "kardex/index.html"
