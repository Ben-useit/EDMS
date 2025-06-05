from django.utils.translation import gettext_lazy as _

from mayan.apps.smart_settings.settings import setting_cluster

from .literals import DEFAULT_FUNDRAISERS_DISABLED

setting_namespace = setting_cluster.do_namespace_add(
    label=_(message='Fundraisers'), name='fundraisers'
)

setting_fundraisers_enable = setting_namespace.do_setting_add(
    choices=('false', 'true'), default=DEFAULT_FUNDRAISERS_DISABLED,
    global_name='FUNDRAISERS_DISABLED', help_text=_(
        message='Disable the fundraiser client.'
    )
)
