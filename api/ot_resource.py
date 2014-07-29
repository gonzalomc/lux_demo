from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from webapp.models.ot_model import Ot
from tastypie import fields
from api.ot_image import OtImageResource

class OtResource(ModelResource):
    image = fields.ToManyField('api.ot_image.OtImageResource', 'image', full=True)

    class Meta:
        queryset = Ot.objects.all()
        resource_name = 'ot'
        serializer = Serializer(formats=['json',])




