from django.apps import apps
from django.contrib import admindocs
from django.utils.translation import gettext as _

from mayan.apps.databases.classes import ModelAttribute
from mayan.apps.forms import form_widgets

from .template_backends import Template


class FormWidgetCode(form_widgets.Textarea):
    template_name = 'templating/forms/widgets/code.html'


class TemplateWidget(form_widgets.NamedMultiWidget):
    builtin_excludes = {
        'tags': ('csrf_token',)
    }

    subwidgets = {
        'builtin_tags': form_widgets.Select(
            attrs={
                'data-autocopy': 'true',
                'data-field-template': '${ $this.val() }'
            }
        ),
        'template': FormWidgetCode(
            attrs={
                'data-template-fields': 'template',
                'rows': 5
            }
        )
    }

    class Media:
        js = ('templating/js/template_widget.js',)

    def decompress(self, value):
        choices_builtin = []
        choices_builtin.append(
            (
                _(message='Filters'), self.get_builtin_choices(
                    klass='filters', name_template='{{{{ | {} }}}}'
                )
            )
        )
        choices_builtin.append(
            (
                _(message='Tags'), self.get_builtin_choices(
                    klass='tags', name_template='{{% {} %}}'
                )
            )
        )
        choices_builtin.insert(
            0, (
                '', _(message='<Filters and tags>')
            )
        )

        self.widgets['builtin_tags'].choices = choices_builtin
        return {
            'builtin_tags': None, 'template': value
        }

    def get_builtin_choices(self, klass, name_template='{}'):
        result = []
        template = Template('')
        builtin_libraries = [
            ('', library) for library in template._template.backend.engine.template_builtins
        ]
        for module_name, library in builtin_libraries:
            for name, function in getattr(library, klass).items():
                if name not in self.builtin_excludes.get(klass, ()):
                    title, body, metadata = admindocs.utils.parse_docstring(
                        function.__doc__
                    )
                    title = _(title)
                    result.append(
                        (
                            name_template.format(name), '{} - {}'.format(
                                name, title
                            )
                        )
                    )

        result = sorted(
            result, key=lambda x: x[0]
        )

        return result

    def get_context(self, name, value, attrs):
        result = super().get_context(attrs=attrs, name=name, value=value)
        # Set builtin_tags autocopy sub widget as not required.
        result['widget']['subwidgets'][0]['attrs']['class'] = 'form-control select2-templating'
        result['widget']['subwidgets'][0]['attrs']['required'] = False
        return result

    def value_from_datadict(self, querydict, files, name):
        template = querydict.get(
            '{}_template'.format(name)
        )

        return template


class ModelTemplateWidget(TemplateWidget):
    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs=attrs, **kwargs)
        self.widgets['model_attribute'] = form_widgets.Select(
            attrs={
                'data-autocopy': 'true',
                'data-field-template': '{{ ${ $idTemplate.data("model-variable") }.${ $this.val() } }}'
            }
        )
        self.subwidgets_order.insert(0, 'model_attribute')

    def decompress(self, value):
        result = super().decompress(value=value)

        model = apps.get_model(
            app_label=self.attrs['app_label'],
            model_name=self.attrs['model_name']
        )

        attribute_choices = ModelAttribute.get_all_choices_for(model=model)
        attribute_choices.insert(
            0, (
                '', _(message='<Model attributes>')
            )
        )

        self.widgets['model_attribute'].choices = attribute_choices

        result['model_attribute'] = None

        return result

    def get_context(self, name, value, attrs):
        result = super().get_context(attrs=attrs, name=name, value=value)
        # Set model_attribute autocopy sub widget as not required.
        result['widget']['subwidgets'][1]['attrs']['class'] = 'form-control select2-templating'
        result['widget']['subwidgets'][1]['attrs']['required'] = False
        return result
