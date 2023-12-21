from rest_framework.generics import ListAPIView
from apps.module.models import Course
from apps.module.api_endpoints.CourseList.serializers import CourseListSerializer


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer


__all__ = ['CourseListView']
