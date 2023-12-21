import factory
from apps.module.models import Drug


class DrugFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Drug

    title = factory.Faker('word')


__all__ = ['DrugFactory']
