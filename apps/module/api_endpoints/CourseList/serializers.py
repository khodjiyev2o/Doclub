from rest_framework import serializers
from apps.module.models import Course


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'description',
            'image',
            'speaker',
        )


__all__ = ['CourseListSerializer']