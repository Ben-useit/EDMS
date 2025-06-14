import logging

from django.utils.translation import gettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import (
    permission_acl_edit, permission_acl_view
)
from mayan.apps.app_manager.apps import MayanAppConfig
from mayan.apps.common.classes import ModelCopy
from mayan.apps.common.menus import (
    menu_multi_item, menu_object, menu_return, menu_secondary, menu_setup
)
from mayan.apps.events.classes import EventModelRegistry, ModelEventType
from mayan.apps.forms import column_widgets
from mayan.apps.navigation.source_columns import SourceColumn
from mayan.apps.rest_api.fields import DynamicSerializerField

from .events import event_announcement_edited
from .links import (
    link_announcement_create, link_announcement_delete_multiple,
    link_announcement_delete_single, link_announcement_edit,
    link_announcement_list, link_announcement_setup
)
from .permissions import (
    permission_announcement_delete, permission_announcement_edit,
    permission_announcement_view
)

logger = logging.getLogger(name=__name__)


class AnnouncementsApp(MayanAppConfig):
    app_namespace = 'announcements'
    app_url = 'announcements'
    has_rest_api = True
    has_tests = True
    name = 'mayan.apps.announcements'
    verbose_name = _(message='Announcements')

    def ready(self):
        super().ready()

        Announcement = self.get_model(model_name='Announcement')

        DynamicSerializerField.add_serializer(
            klass=Announcement,
            serializer_class='mayan.apps.announcements.serializers.AnnouncementSerializer'
        )

        EventModelRegistry.register(model=Announcement)

        ModelCopy(
            model=Announcement, bind_link=True, register_permission=True
        ).add_fields(
            field_names=(
                'label', 'text', 'enabled', 'start_datetime', 'end_datetime'
            )
        )

        ModelEventType.register(
            model=Announcement, event_types=(event_announcement_edited,)
        )

        ModelPermission.register(
            model=Announcement, permissions=(
                permission_acl_edit, permission_acl_view,
                permission_announcement_delete, permission_announcement_edit,
                permission_announcement_view
            )
        )
        SourceColumn(
            attribute='label', is_identifier=True, is_sortable=True,
            source=Announcement
        )
        SourceColumn(
            attribute='enabled', include_label=True, is_sortable=True,
            source=Announcement, widget=column_widgets.TwoStateWidget
        )
        SourceColumn(
            attribute='start_datetime', empty_value=_(message='None'),
            include_label=True, is_sortable=True, source=Announcement
        )
        SourceColumn(
            attribute='end_datetime', empty_value=_(message='None'),
            include_label=True, is_sortable=True, source=Announcement
        )

        menu_multi_item.bind_links(
            links=(link_announcement_delete_multiple,),
            sources=(Announcement,)
        )
        menu_object.bind_links(
            links=(
                link_announcement_delete_single, link_announcement_edit
            ), sources=(Announcement,)
        )
        menu_return.bind_links(
            links=(link_announcement_list,),
            sources=(
                Announcement, 'announcements:announcement_list',
                'announcements:announcement_create'
            )
        )
        menu_secondary.bind_links(
            links=(link_announcement_create,),
            sources=(
                Announcement, 'announcements:announcement_list',
                'announcements:announcement_create'
            )
        )
        menu_setup.bind_links(
            links=(link_announcement_setup,)
        )
