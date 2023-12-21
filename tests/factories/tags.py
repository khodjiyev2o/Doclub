import factory
from apps.common.models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    title = factory.Faker('word')


__all__ = ['TagFactory']
