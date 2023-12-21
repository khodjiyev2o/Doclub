import factory
from apps.module.models import PharmacistCompany


class PharmacistCompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PharmacistCompany

    title = factory.Faker('word')


__all__ = ['PharmacistCompanyFactory']
