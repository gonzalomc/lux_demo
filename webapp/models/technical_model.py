from django.db import models


class Technical(models.Model):
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)

    def  __unicode__(self):
        return self.name

    class Meta:
        app_label = 'webapp'
        db_table = 'technical'

