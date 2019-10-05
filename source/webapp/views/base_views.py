from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, render, redirect


class DetailView(TemplateView):
    context_key = 'object'
    model = None

    def get_context_data(self, **kwargs):
        pk = kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context


class UpdateView(View):
    form_class = None
    template_name = None
    model = None
    redirect_url = None
    key_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})

    def get_object(self):
        pk = self.kwargs.get(self.key_kwarg)
        return get_object_or_404(self.model, pk=pk)