from rest_framework.generics import RetrieveAPIView
from apps.module.models import Course
from apps.module.api_endpoints.CourseDetail.serializers import CourseDetailSerializer


class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.prefetch_related('drugs', 'speaker', 'modules', 'pharmacist_company')
    serializer_class = CourseDetailSerializer


__all__ = ['CourseDetailView']
