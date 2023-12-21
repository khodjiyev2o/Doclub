import factory
from apps.module.models import Certificate


class CertificateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Certificate

    course = factory.SubFactory("tests.factories.course.CourseFactory")
    user = factory.SubFactory("tests.factories.user.UserFactory")
    file = factory.django.FileField(filename='certificate.pdf')


__all__ = ['CertificateFactory']

