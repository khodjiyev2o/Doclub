from rest_framework import serializers
from apps.module.models import UserModuleCompletionRequirements


class UserModuleCompletionRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModuleCompletionRequirements
        fields = (
            'is_video_played',
            'is_files_downloaded',
            'is_test_passed',
            'can_certificate_be_issued'
        )


class UserModuleCompletionRequirementsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModuleCompletionRequirements
        fields = (
            'is_video_played',
            'is_files_downloaded',
            'is_test_passed',
        )
