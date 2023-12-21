import factory
from django.core.files.base import ContentFile
from apps.module.models import Course
from .drug import DrugFactory
from .pharmacist_company import PharmacistCompanyFactory


def create_certificate_template():
    content = "<html>My custom HTML content with {{ placeholders }}</html>"
    return ContentFile(content, 'template.html')


certificate_html_template = factory.django.FileField(from_func=create_certificate_template)


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text', max_nb_chars=200)
    image = factory.django.ImageField(color='green')
    disclaimer = factory.Faker('text', max_nb_chars=500)
    certificate_html_template = certificate_html_template
    drug = factory.RelatedFactoryList(
        DrugFactory,
        size=4,
    )
    pharmacist_company = factory.RelatedFactoryList(
        PharmacistCompanyFactory,
        size=4,
    )