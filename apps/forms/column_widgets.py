from mayan.apps.navigation.column_widgets import SourceColumnWidget

from .icons import icon_fail as default_icon_fail, icon_ok as default_icon_ok


class TwoStateWidget(SourceColumnWidget):
    template_name = 'forms/two_state_widget.html'

    def __init__(self, icon_ok=None, icon_fail=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon_ok = icon_ok or default_icon_ok
        self.icon_fail = icon_fail or default_icon_fail

    def get_extra_context(self):
        return {
            'icon_fail': self.icon_fail, 'icon_ok': self.icon_ok
        }


class ObjectLinkWidget(SourceColumnWidget):
    template_string = '<a href="{{ url }}">{{ object_type }}{{ label }}</a>'

    def get_extra_context(self):
        label = ''
        object_type = ''
        url = None

        if self.value:
            label = str(self.value)
            try:
                object_type = '{}: '.format(self.value._meta.verbose_name)
            except AttributeError:
                object_type = ''

            try:
                url = self.value.get_absolute_url()
            except AttributeError:
                url = None

            if getattr(self.value, 'is_staff', None) or getattr(self.value, 'is_superuser', None):
                # Don't display a anchor to for the user details view for
                # super users and staff, the details view filters them.
                # Staff and admin users are not manageable by the normal
                # user views.
                url = '#'
                label = '{}{}'.format(object_type, label)

        return {
            'label': label, 'object_type': object_type,
            'url': url or '#'
        }
