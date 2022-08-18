from django.views.generic import TemplateView


class PortadaView(TemplateView):
    template_name = "kardex/index.html"