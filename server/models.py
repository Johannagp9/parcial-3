from datetime import datetime

from django.db import models

# Create your models here.
from mongoengine import Document, StringField, DateTimeField, EmailField


class Mensaje(Document):
    origen = EmailField(null=False)
    destino = EmailField(null=False)
    contenido = StringField(null=False)
    fecha = DateTimeField(default=datetime.utcnow)
    foto = StringField(null=True)

    def __str__(self):
        return self.contenido



