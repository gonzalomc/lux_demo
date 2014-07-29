from django.contrib import admin
from models.ot_model import Ot
from models.otimage_model import OtImage
from models.section_model import Section
from models.field_model import Field
from models.technical_model import Technical
from models.client import Client
from models.product import Product

admin.site.register(Ot)
admin.site.register(Section)
admin.site.register(Field)
admin.site.register(OtImage)
admin.site.register(Technical)
admin.site.register(Client)
admin.site.register(Product)