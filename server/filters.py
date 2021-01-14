import django_mongoengine_filter

from server.models import Mensaje


class MensajeFilter(django_mongoengine_filter.FilterSet):
    contenido = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')
    class Meta:
        model = Mensaje
        fields = ['fecha','origen','destino']

