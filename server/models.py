from datetime import datetime

from django.db import models

# Create your models here.
from mongoengine import Document, StringField, DateTimeField, EmailField, ReferenceField, IntField


class Mensaje(Document):
    origen = EmailField(null=False)
    destino = EmailField(null=False)
    contenido = StringField(null=False)
    fecha = DateTimeField(default=datetime.utcnow)
    foto = StringField(null=True)

    def __str__(self):
        return self.contenido

class Usuario(Document):
    google_id = StringField()
    email = EmailField()
    def __str__(self):
        return self.email


class Imagen(Document):
    usuario = ReferenceField(Usuario)
    descripcion = StringField(null=False)
    foto = StringField(null=True)
    likes = IntField(default=0)


