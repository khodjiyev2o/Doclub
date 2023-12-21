from rest_framework import serializers
from apps.module.models import Course, Speaker, Drug, PharmacistCompany, CourseFiles


class CourseDetailPharmacistCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacistCompany
        fields = (
            'id',
            'title',
        )


class CourseDetailDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = (
            'id',
            'title',
        )


class CourseDetailSpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = (
            'first_name',
            'last_name',
            'family_name',
            'position',
            'avatar'
        )


class CourseDetailCourseFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFiles
        fields = (
            'id',
            'title',
            'file',
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    speaker = CourseDetailSpeakerSerializer(many=True)
    drugs = CourseDetailDrugSerializer(many=True)
    pharmacist_company = CourseDetailPharmacistCompanySerializer(many=True)
    course_files = CourseDetailCourseFilesSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'description',
            'image',
            'speaker',
            'drugs',
            'pharmacist_company',
            'disclaimer',
            'course_files',
            'number_of_modules'
        )


__all__ = ['CourseDetailSerializer']
