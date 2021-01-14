from datetime import datetime

from django.db import models

# Create your models here.
from mongoengine import Document, StringField, DateTimeField, ReferenceField, EmailField


class Mensaje(Document):
    origen = EmailField(null=False)
    destino = EmailField(null=False)
    contenido = StringField(null=False)
    fecha = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.contenido



