from rest_framework import serializers

from apps.module.models import Certificate, Course


class GenerateCertificateSerializer(serializers.Serializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ("id", "course", "user", "cid", "file", "created_at", "updated_at")
