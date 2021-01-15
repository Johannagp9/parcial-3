import django_mongoengine_filter

from server.models import Mensaje, Imagen, Usuario


class MensajeFilter(django_mongoengine_filter.FilterSet):
    contenido = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')
    class Meta:
        model = Mensaje
        fields = ['fecha','origen','destino']

class ImagenFilter(django_mongoengine_filter.FilterSet):
    descripcion = django_mongoengine_filter.filters.StringFilter(lookup_type='icontains')
    class Meta:
        model = Imagen
        fields = ['likes']

class UsuarioFilter(django_mongoengine_filter.FilterSet):
    class Meta:
        model = Usuario
        fields = ['email','google_id']