from django.db import  models
from webapp.models.technical_model import Technical
from webapp.models.product import Product

class Ot(models.Model):

    status_choices = (
        ('1' , 'abierta'),
        ('2' , 'pendiente'),
        ('3' , 'cerrada'),
    )
    description = models.TextField()
    status = models.CharField(max_length=50, choices=status_choices, default='1')
    technical = models.ForeignKey(Technical, related_name='technical', null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __unicode__(self):
        return self.description

    class Meta:
        app_label = 'webapp'
        db_table = 'ot'
        permissions = (
            ("view_ot", "Can View Ot"),
        )
