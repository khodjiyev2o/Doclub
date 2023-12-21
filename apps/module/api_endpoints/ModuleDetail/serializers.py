from rest_framework import serializers
from apps.module.models import Module, Speaker, Drug, PharmacistCompany, CourseFiles


class ModuleDetailPharmacistCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacistCompany
        fields = (
            'id',
            'title',
        )


class ModuleDetailDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = (
            'id',
            'title',
        )


class ModuleDetailSpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = (
            'first_name',
            'last_name',
            'family_name',
            'position',
            'avatar'
        )


class ModuleDetailCourseFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFiles
        fields = (
            'id',
            'title',
            'file',
        )


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = (
            'id',
            'title',
            'cover_image',
            'tags',
            'speaker',
            'drugs',
            'pharmacist_company',
            'module_files',
            'disclaimer',
        )


__all__ = ['ModuleSerializer']
