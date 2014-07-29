from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import Group
from webapp.models.ot_model import Ot
from braces.views import LoginRequiredMixin
from webapp.forms.admin_forms import PermissionGroup
from django.http import HttpResponseRedirect



class PermissionView(LoginRequiredMixin, TemplateView):
    template_name = 'private/admin/permission.html'

    def get_context_data(self, **kwargs):
        context = super(PermissionView, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        context['ot'] = Ot
        return context


class PermissionDetailView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'private/admin/permission_detail.html'
    form_class = PermissionGroup

    def post(self, request, *args, **kwargs):
        self.object = Group.objects.get(id=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        permiso = form.save(commit=False)
        permiso.save()
        form.save_m2m()
        return HttpResponseRedirect('/permisos/%s' % permiso.id)


    def form_invalid(self, form):
        return super(PermissionDetailView, self).form_invalid(form)

