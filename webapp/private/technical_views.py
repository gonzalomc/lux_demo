from django.views.generic import ListView, DetailView, CreateView
from webapp.models.technical_model import Technical
from webapp.forms.technical_forms import TechnicalCreateForm
from django.http import HttpResponseRedirect

class TechnicalListView(ListView):
    model = Technical
    template_name = 'private/technical/list.html'
    context_object_name = 'techs'


class TechnicalCreateView(CreateView):
    model = Technical
    template_name = 'private/technical/create.html'
    form_class = TechnicalCreateForm

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_tech = form.save()
        return HttpResponseRedirect('/tecnicos/%s' % new_tech.id)

    def form_invalid(self, form):
        return super(TechnicalCreateView, self).form_invalid(form)


class TechnicalDetailView(DetailView):
    model = Technical
    template_name = 'private/technical/detail.html'
    context_object_name = 'tech'
