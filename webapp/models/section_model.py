from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200, blank=True)
    default = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'webapp'
        db_table = 'sections'
