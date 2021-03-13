from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return str(self.pk)

