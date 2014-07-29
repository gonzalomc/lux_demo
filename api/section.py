from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from webapp.models.section_model import Section
from tastypie import fields
from tastypie.authorization import Authorization

class SectionResource(ModelResource):

    field = fields.ToManyField('api.field.FieldResource', 'field', related_name='section', full=True, null=True)

    class Meta:
        queryset = Section.objects.all()
        resource_name = 'section'
        serializer = Serializer(formats=['json',])
        authorization = Authorization()

