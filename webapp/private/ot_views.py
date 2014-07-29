from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import DetailView, CreateView, UpdateView
from braces.views import GroupRequiredMixin
from webapp.models.ot_model import Ot
from webapp.forms.ot_forms import OtForm


class OtDetailView(DetailView):
    template_name = 'private/ot/detail.html'
    context_object_name = 'ot'
    model = Ot


class OtCreateView(CreateView):
    model = Ot
    template_name = 'private/ot/create.html'
    form_class = OtForm

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_ot = form.save(commit=False)
        new_ot.save()
        form.save_m2m()
        return HttpResponseRedirect('/ot/%s' % new_ot.id)


    def form_invalid(self, form):
        return super(OtCreateView, self).form_invalid(form)


class OtUpdateView(UpdateView):
    template_name = 'private/ot/update.html'
    context_object_name = 'ot'
    model = Ot

    def post(self, request, *args, **kwargs):
        self.object = Ot.objects.get(id=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_ot = form.save(commit=False)
        new_ot.save()
        form.save_m2m()
        return HttpResponseRedirect('/ot/%s' % new_ot.id)


    def form_invalid(self, form):
        return super(OtCreateView, self).form_invalid(form)
