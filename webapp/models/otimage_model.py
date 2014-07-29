from django.db import models
from webapp.models.ot_model import Ot


class OtImage(models.Model):
    ot = models.ForeignKey(Ot, related_name='image')
    image = models.ImageField(upload_to='ot_images')

    def __unicode__(self):
        return "%s - %s" % (self.ot.id, self.ot.description)

    class Meta:
        app_label = 'webapp'
        db_table = 'ot_images'
