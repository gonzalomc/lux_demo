from django.db import models
from webapp.models.section_model import Section

class Field(models.Model):

    type_choices = (
        ('text', 'text'),
        ('array', 'array'),
        ('select', 'select'),
    )
    name = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, choices=type_choices, default='text')
    section = models.ForeignKey(Section, related_name='field')

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'webapp'
        db_table = 'fields'
