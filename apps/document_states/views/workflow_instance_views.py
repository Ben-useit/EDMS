from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.models import AccessControlList
from mayan.apps.documents.models.document_models import Document
from mayan.apps.forms import forms
from mayan.apps.views.generics import FormView, SingleObjectListView
from mayan.apps.views.view_mixins import ExternalObjectViewMixin

from ..forms.workflow_instance_forms import (
    WorkflowInstanceTransitionSelectForm
)
from ..icons import (
    icon_workflow_instance_detail, icon_workflow_instance_list,
    icon_workflow_instance_transition,
    icon_workflow_instance_transition_select, icon_workflow_template_list
)
from ..links import link_workflow_instance_transition
from ..models import WorkflowInstance
from ..permissions import (
    permission_workflow_instance_transition, permission_workflow_template_view
)


class WorkflowInstanceListView(ExternalObjectViewMixin, SingleObjectListView):
    external_object_permission = permission_workflow_template_view
    external_object_pk_url_kwarg = 'document_id'
    external_object_queryset = Document.valid.all()
    object_permission = permission_workflow_template_view
    view_icon = icon_workflow_instance_list

    def get_extra_context(self):
        return {
            'hide_link': True,
            'no_results_icon': icon_workflow_template_list,
            'no_results_text': _(
                message='Assign workflows to the document type of this document '
                'to have this document execute those workflows. '
            ),
            'no_results_title': _(
                message='There are no workflows for this document'
            ),
            'object': self.external_object,
            'title': _(
                message='Workflows for document: %s'
            ) % self.external_object
        }

    def get_source_queryset(self):
        return self.external_object.workflows.all()


class WorkflowInstanceDetailView(
    ExternalObjectViewMixin, SingleObjectListView
):
    external_object_permission = permission_workflow_template_view
    external_object_pk_url_kwarg = 'workflow_instance_id'
    object_permission = permission_workflow_template_view
    view_icon = icon_workflow_instance_detail

    def get_extra_context(self):
        return {
            'hide_object': True,
            'navigation_object_list': ('object', 'workflow_instance'),
            'no_results_icon': icon_workflow_instance_detail,
            'no_results_main_link': link_workflow_instance_transition.resolve(
                context=RequestContext(
                    dict_={'object': self.external_object},
                    request=self.request
                )
            ),
            'no_results_text': _(
                message='This view will show the state changes as a workflow '
                'instance is transitioned.'
            ),
            'no_results_title': _(
                message='There are no details for this workflow instance'
            ),
            'object': self.external_object.document,
            'title': _(message='Detail of workflow: %(workflow)s') % {
                'workflow': self.external_object
            },
            'workflow_instance': self.external_object
        }

    def get_external_object_queryset(self):
        queryset_documents = AccessControlList.objects.restrict_queryset(
            queryset=Document.valid.all(),
            permission=permission_workflow_template_view,
            user=self.request.user
        )

        return WorkflowInstance.objects.filter(
            document_id__in=queryset_documents.values('pk')
        )

    def get_source_queryset(self):
        return self.external_object.log_entries.order_by('-datetime')


class WorkflowInstanceTransitionExecuteView(
    ExternalObjectViewMixin, FormView
):
    external_object_pk_url_kwarg = 'workflow_instance_id'
    external_object_queryset = WorkflowInstance.valid.all()
    form_class = forms.DynamicForm
    template_name = 'appearance/form_container.html'
    view_icon = icon_workflow_instance_transition

    def form_valid(self, form):
        form_data = form.cleaned_data
        comment = form_data.pop('comment')

        self.external_object.do_transition(
            comment=comment, extra_data=form_data,
            transition=self.get_workflow_template_transition(),
            user=self.request.user
        )
        messages.success(
            message=_(
                message='Document "%s" transitioned successfully'
            ) % self.external_object.document, request=self.request
        )
        return HttpResponseRedirect(
            redirect_to=self.get_success_url()
        )

    def get_external_object_queryset_filtered(self):
        queryset = super().get_external_object_queryset_filtered()

        # Filter further down by document access.
        queryset_documents = AccessControlList.objects.restrict_queryset(
            permission=permission_workflow_instance_transition,
            queryset=Document.valid.all(),
            user=self.request.user
        )

        return queryset.filter(document__in=queryset_documents)

    def get_extra_context(self):
        return {
            'navigation_object_list': ('object', 'workflow_instance'),
            'object': self.external_object.document,
            'title': _(
                message='Execute transition "%(transition)s" for workflow: '
                '%(workflow)s'
            ) % {
                'transition': self.get_workflow_template_transition(),
                'workflow': self.external_object
            },
            'workflow_instance': self.external_object
        }

    def get_form_extra_kwargs(self):
        schema = {
            'fields': {
                'comment': {
                    'label': _(message='Comment'),
                    'class': 'django.forms.CharField', 'kwargs': {
                        'help_text': _(
                            message='Optional comment to attach to the '
                            'transition.'
                        ),
                        'required': False,
                    }
                }
            },
            'widgets': {
                'comment': {
                    'class': 'django.forms.widgets.Textarea',
                    'kwargs': {
                        'attrs': {'rows': 3}
                    }
                }
            }
        }

        workflow_template_transition = self.get_workflow_template_transition()
        workflow_template_transition.get_form_schema(
            schema=schema, workflow_instance=self.external_object
        )

        return {'schema': schema}

    def get_success_url(self):
        return self.external_object.get_absolute_url()

    def get_workflow_template_transition(self):
        return get_object_or_404(
            klass=self.external_object.get_queryset_valid_transitions(
                user=self.request.user
            ), pk=self.kwargs['workflow_template_transition_id']
        )


class WorkflowInstanceTransitionSelectView(
    ExternalObjectViewMixin, FormView
):
    external_object_pk_url_kwarg = 'workflow_instance_id'
    external_object_queryset = WorkflowInstance.valid.all()
    form_class = WorkflowInstanceTransitionSelectForm
    template_name = 'appearance/form_container.html'
    view_icon = icon_workflow_instance_transition_select

    def form_valid(self, form):
        return HttpResponseRedirect(
            redirect_to=reverse(
                kwargs={
                    'workflow_instance_id': self.external_object.pk,
                    'workflow_template_transition_id': form.cleaned_data['transition'].pk
                },
                viewname='document_states:workflow_instance_transition_execute'
            )
        )

    def get_extra_context(self):
        return {
            'navigation_object_list': ('object', 'workflow_instance'),
            'object': self.external_object.document,
            'submit_label': _(message='Select'),
            'title': _(
                message='Select transition for workflow "%(workflow)s" of document "%(document)s"'
            ) % {
                'document': self.external_object.document,
                'workflow': self.external_object
            },
            'workflow_instance': self.external_object
        }

    def get_external_object_queryset_filtered(self):
        queryset = super().get_external_object_queryset_filtered()

        # Filter further down by document access.
        queryset_documents = AccessControlList.objects.restrict_queryset(
            permission=permission_workflow_instance_transition,
            queryset=Document.valid.all(),
            user=self.request.user
        )

        return queryset.filter(document__in=queryset_documents)

    def get_form_extra_kwargs(self):
        return {
            'user': self.request.user,
            'workflow_instance': self.external_object
        }
