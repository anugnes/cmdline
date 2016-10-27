from django.db import models
import uuid


class Server(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField("Hostname", max_length=50)
    is_live = models.BooleanField("Live server")
    ssh_key = models.TextField("SSH key", max_length=512)


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    is_root = models.BooleanField()
    is_sudo = models.BooleanField()

