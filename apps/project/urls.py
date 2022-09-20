from django.urls import include, path
from rest_framework import routers

from apps.project.views import (
    UpdateDataView, ProjectCreateView, ProjectUpdateView,
    VersionListView, VersionCreateView, VersionCopyView,
    VersionUpdateView, RegisterListView, RegisterCreateView, RegisterUpdateView,
    RegisterViewSet, FieldViewSet, FieldChoiceViewSet, FileUploadView, FileDownloadView, FieldListView, VersionViewSet
)

router = routers.DefaultRouter()
router.register(r'registers', RegisterViewSet)
router.register(r'versions', VersionViewSet)
router.register(r'fields-list', FieldViewSet)
router.register(r'field-choices', FieldChoiceViewSet)

app_name = 'project'

urlpatterns = [
    path('', include(router.urls)),

    # Project
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),

    # Version
    path('<int:pk>/versions/', VersionListView.as_view(), name='version-list'),
    path('version-create/', VersionCreateView.as_view(), name='version-create'),
    path('version-update/<int:pk>/', VersionUpdateView.as_view(), name='version-update'),
    path('version-copy/', VersionCopyView.as_view(), name='version-copy'),

    # Register
    path('<int:pk>/registers/', RegisterListView.as_view(), name='register-list'),
    path('register-create/', RegisterCreateView.as_view(), name='register-create'),
    path('register-update/<int:pk>/', RegisterUpdateView.as_view(), name='register-update'),
    path('fileUpload/', FileUploadView.as_view(), name='file-upload'),
    path('<int:pk>/registers/fileDownload/', FileDownloadView.as_view(), name='file-download'),
    path('fields/',FieldListView.as_view(), name='field-list'),
    path('updateData/', UpdateDataView.as_view(), name='update-data'),
]
