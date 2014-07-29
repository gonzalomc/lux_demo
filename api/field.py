from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from tastypie import fields
from webapp.models.field_model import Field


class FieldResource(ModelResource):
    section = fields.ToOneField('api.section.SectionResource', 'section')

    class Meta:
        queryset = Field.objects.all()
        resource_name = 'field'
        serializer = Serializer(formats=['json',])
