from django.contrib.auth.models import Permission, Group, ContentType
from django import forms

class PermissionGroup(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super (PermissionGroup, self ).__init__(*args,**kwargs) # populates the post
        self.fields['permissions'].queryset = Permission.objects.filter(content_type=ContentType.objects.filter(app_label='webapp'))

    class Meta:
        model = Group
