from __future__ import unicode_literals
from django.conf import settings
from django.db import models

class Device(models.Model):
    ip_address = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sshport = models.IntegerField(default=22)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {} - {}".format(self.id, self.ip_address, self.hostname)

class Log(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    host = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    messages = models.CharField(max_length=255, blank=True)
    commandline = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.host, self.action, self.status)