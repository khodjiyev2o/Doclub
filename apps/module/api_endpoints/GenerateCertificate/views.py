from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CertificateSerializer, GenerateCertificateSerializer

from apps.module.models import Certificate, Course


class GenerateCertificateAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GenerateCertificateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = serializer.validated_data["course"]

        if Certificate.objects.filter(course=course, user=request.user).exists():
            data = CertificateSerializer(
                Certificate.objects.get(course=course, user=request.user), context={"request": request}
            ).data
            return Response(data=data, status=status.HTTP_200_OK)
        can_course_certificate_be_issued = Course.objects.get(id=course.id).can_course_certificate_be_issued(
            user=self.request.user)

        if not can_course_certificate_be_issued:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        certificate = Certificate.objects.create(user=self.request.user, course=course)
        return Response(
            data=CertificateSerializer(certificate, context={"request": request}).data, status=status.HTTP_201_CREATED
        )


__all__ = ['GenerateCertificateAPIView']
