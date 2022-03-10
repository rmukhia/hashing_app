from django.db import models


class RequestLog(models.Model):
    query = models.TextField()
    timestamp = models.DateTimeField()
    hash = models.CharField(max_length=256)

    def __str__(self):
        return f"[{int(self.timestamp.timestamp())}] {self.query[:24]}"
