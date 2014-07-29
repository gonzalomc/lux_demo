from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'webapp'
        db_table = 'product'
