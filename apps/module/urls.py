from django.urls import path
from .api_endpoints import * # noqa

urlpatterns = [
    path("CourseList/", CourseListView.as_view(), name="course-list"),
    path("CourseDetail/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("MOduleDetail/<int:pk>/", ModuleDetailView.as_view(), name="module-detail"),
    path("ModuleRequirements/<int:pk>/", UserModuleRequirementsView.as_view(), name="user-module-requirements"),
    path("ModuleRequirementsUpdate/<int:pk>/", UserModuleRequirementsUpdateView.as_view(),
         name="user-module-requirements-update"),
    path("GenerateCertificate/", GenerateCertificateAPIView.as_view(), name="generate-certificate"),
]
