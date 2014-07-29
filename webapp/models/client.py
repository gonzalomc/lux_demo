from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'webapp'
        db_table = 'client'
