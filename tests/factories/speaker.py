import factory
from apps.module.models import Speaker


class SpeakerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Speaker

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    family_name = factory.Faker('last_name')
    position = factory.Faker('job')

    avatar = factory.django.ImageField(color='blue')  # Adjust as needed for your specific use case


__all__ = ['SpeakerFactory']
