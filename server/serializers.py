from rest_framework_mongoengine import serializers

from server.models import Mensaje, Imagen, Usuario


class MensajeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'

class UsuarioSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ImagenSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'