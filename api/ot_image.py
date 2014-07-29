from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from webapp.models.otimage_model import OtImage
from tastypie import fields


class OtImageResource(ModelResource):
    ot = fields.ToOneField('api.ot_resource.OtResource', 'ot')

    class Meta:
        queryset = OtImage.objects.all()
        resource_name = 'image'
        serializer = Serializer(formats=['json'])


