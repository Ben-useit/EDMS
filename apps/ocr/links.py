from django.utils.translation import gettext_lazy as _

from mayan.apps.navigation.links import Link

from .icons import (
    icon_document_type_ocr_settings, icon_document_type_ocr_submit,
    icon_document_version_ocr_content_delete_multiple,
    icon_document_version_ocr_content_delete_single,
    icon_document_version_ocr_content_detail,
    icon_document_version_ocr_content_download,
    icon_document_version_ocr_submit_multiple,
    icon_document_version_ocr_submit_single,
    icon_document_version_page_ocr_content_detail,
    icon_document_version_page_ocr_content_edit
)
from .permissions import (
    permission_document_type_ocr_setup, permission_document_version_ocr,
    permission_document_version_ocr_content_edit,
    permission_document_version_ocr_content_view
)

# Document type

link_document_type_ocr_settings = Link(
    args='resolved_object.id', icon=icon_document_type_ocr_settings,
    permission=permission_document_type_ocr_setup,
    text=_(message='OCR setup'), view='ocr:document_type_ocr_settings'
)
link_document_type_submit = Link(
    icon=icon_document_type_ocr_submit,
    permission=permission_document_version_ocr,
    text=_(message='OCR documents per type'), view='ocr:document_type_submit'
)

# Document version

link_document_version_ocr_content_delete_multiple = Link(
    icon=icon_document_version_ocr_content_delete_multiple,
    text=_(message='Delete OCR content'),
    view='ocr:document_version_ocr_content_multiple_delete'
)
link_document_version_ocr_content_delete_single = Link(
    args='resolved_object.id',
    icon=icon_document_version_ocr_content_delete_single,
    permission=permission_document_version_ocr,
    text=_(message='Delete OCR content'),
    view='ocr:document_version_ocr_content_single_delete'
)
link_document_version_ocr_content_detail = Link(
    args='resolved_object.id',
    icon=icon_document_version_ocr_content_detail,
    permission=permission_document_version_ocr_content_view,
    text=_(message='OCR'), view='ocr:document_version_ocr_content_view'
)
link_document_version_ocr_content_download = Link(
    args='resolved_object.id',
    icon=icon_document_version_ocr_content_download,
    permission=permission_document_version_ocr_content_view,
    text=_(message='Download OCR text'),
    view='ocr:document_version_ocr_content_download'
)
link_document_version_ocr_submit_multiple = Link(
    icon=icon_document_version_ocr_submit_multiple,
    text=_(message='Submit for OCR'), view='ocr:document_version_ocr_multiple_submit'
)
link_document_version_ocr_submit_single = Link(
    args='resolved_object.id',
    icon=icon_document_version_ocr_submit_single,
    permission=permission_document_version_ocr, text=_(message='Submit for OCR'),
    view='ocr:document_version_ocr_single_submit'
)

# Document version page

link_document_version_page_ocr_content_detail_view = Link(
    args='resolved_object.id',
    icon=icon_document_version_page_ocr_content_detail,
    permission=permission_document_version_ocr_content_view,
    text=_(message='OCR'), view='ocr:document_version_page_ocr_content_detail_view'
)
link_document_version_page_ocr_content_edit_view = Link(
    args='resolved_object.id',
    icon=icon_document_version_page_ocr_content_edit,
    permission=permission_document_version_ocr_content_edit,
    text=_(message='Edit OCR'),
    view='ocr:document_version_page_ocr_content_edit_view'
)
