# Django problems

A Django application to report a problem.
A problem is a text description linked to an user and a page.
A problem can be marked as resolved.

## Features
* Link custom data to your problem
* Admin interface to search and filter through all problems
* Compatible with django rest framework
* Automatically create a timestamp when a problem is reported and when a problem is marked as resolved

## Installation

Url
settings.py PROBLEM = {'PAGES': }

## Usage

The application provide 3 simple templates
* problem_form.html : A form to create a problem
* problem_detail.html : Detail view of a problem
* problem_list.html : List view of all problems

You can override them by creating a file with the same name in  `templates/problem` in your app.

If you want to link custom data to your problem, you can follow the steps below.

### Create a model to link custom data
Create a link class in your `models.py`

```python
from problem.models import Problem


class ProblemLink(models.Model):
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)
    mymodel = models.ForeignKey(MyModel, on_delete=models.SET_NULL, null=True)
```


### Create an inline formset  


```python
from problem.models import Problem

from .models import ProblemLink


class ProblemLinkForm(forms.ModelForm):
    class Meta:
        model = ProblemLink
        fields = '__all__'

ProblemLinkFormSet = inlineformset_factory(Problem, ProblemLink, form=ProblemLinkForm, extra=1, can_delete=False)
```

### Create a custom view

Create a subclass of the CreateProblem view and override  `add_formset_to_context` and `validate_formset` methods. Then in problem_form.html you can display the problem_link_formset form


`add_formset_to_context` is called during the `get_context_data` method.

`validate_formset` is called during the `form_valid` method, after the Problem object has been saved.

```python
from probem.views import CreateProblem

from .forms import ProblemLinkFormSet


class CreateProblemLink(CreateProblem):
    def add_formset_to_context(self, context):
        context['problem_link_formset'] = ProblemLinkFormSet()

    def validate_formset(self, request, instance):
        problem_relation_form = ProblemLinkFormSet(request.POST, instance=instance)
        if problem_relation_form.is_valid():
            problem_relation_form.save()
```

In problem_detail.html and problem_list you can simply access `ProblemLink` to display the linked data.

### Custom admin
You can add your custom model as an inline in the admin interface.

```python
from problem.admin import ProblemAdmin
from problem.models import Problem

from .models import ProblemLink

class ProblemLinkInline(admin.StackedInline):
    model = ProblemLink


class CustomizedProblemAdmin(ProblemAdmin):
    inlines = (ProblemLinkInline,)

# Unregister the Problem model, to replace it with yours
admin.site.unregister(Problem)
admin.site.register(Problem, CustomizedProblemAdmin)
```

### With django-rest-framework

A serializer is provided, you can use it to .

```python
from problem.serializers import ProblemSerializer
from problem.models import Problem

from .models import ProblemLink


class ProblemLinkSerializer(ModelSerializer):
    problem = ProblemSerializer()
    class Meta:
        model = ProblemLink
        fields = ['mymodel', 'problem']

    def create(self, validated_data):
        problem = validated_data.pop('problem')
        problem = Problem.objects.create(**problem)
        problem_link = ProblemLink.objects.create(**validated_data, problem=problem)
        return problem_link
```
