from django.urls import reverse_lazy
from django.views import generic

from .forms import ProblemForm
from .models import Problem


class DetailProblem(generic.DetailView):
    model = Problem
    template_name = 'problem/problem_detail.html'


class ListProblem(generic.ListView):
    model = Problem
    template_name = 'problem/problem_list.html'


class CreateProblem(generic.edit.CreateView):
    template_name = 'problem/problem_form.html'
    form_class = ProblemForm

    # Add formset to context
    def add_formset_to_context(self, context):
        """
        Add a formset to the context. Context is a dict.
        """
        pass

    # Save form set
    def validate_formset(self, request, instance):
        """
        Validate and save formset.
        The problem is already created when this method is called.
        """
        pass


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.add_formset_to_context(context)
        return context


    def form_valid(self, form):
        self.object = form.save()
        self.validate_formset(self.request, self.object)
        return super().form_valid(form)
