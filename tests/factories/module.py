import factory
from apps.module.models import Module
from .course import CourseFactory
from .tags import TagFactory
from .drug import DrugFactory
from .pharmacist_company import PharmacistCompanyFactory


class ModuleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Module

    title = factory.Faker('sentence', nb_words=5)
    video = factory.django.FileField(filename='video.mp4')
    cover_image = factory.django.ImageField(color='blue')
    disclaimer = factory.Faker('text', max_nb_chars=500)
    course = factory.SubFactory(CourseFactory)
    tags = factory.RelatedFactoryList(
        TagFactory,
        size=4,
    )
    drug = factory.RelatedFactoryList(
        DrugFactory,
        size=4,
    )
    pharmacist_company = factory.RelatedFactoryList(
        PharmacistCompanyFactory,
        size=4,
    )


__all__ = ['ModuleFactory']
