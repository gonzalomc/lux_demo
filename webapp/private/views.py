from django.contrib.auth.models import User, Group
from django.views.generic import ListView
from webapp.models.ot_model import Ot
from guardian.shortcuts import remove_perm, assign_perm



class OtListView(ListView):
    model = Ot
    template_name = 'private/ot/list.html'
    context_object_name = 'ot_list'
    paginate_by = 3
    queryset = Ot.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(OtListView, self).get_context_data(*args,
                                                           **kwargs)
        # Asignar o Quitar permisos
        #remove_perm('webapp.add_ot', Group.objects.get(name='admins'))
        #assign_perm('webapp.add_ot', Group.objects.get(name='admins'))
        #assign_perm('webapp.change_ot', Group.objects.get(name='admins'))
        #remove_perm('webapp.change_ot', Group.objects.get(name='admins'))
        #assign_perm('webapp.delete_ot', Group.objects.get(name='admins'))
        #remove_perm('webapp.delete_ot', Group.objects.get(name='admins'))
        #assign_perm('webapp.change_ot', Group.objects.get(name='tecnico'))
        #remove_perm('webapp.change_ot', Group.objects.get(name='tecnico'))


        return context