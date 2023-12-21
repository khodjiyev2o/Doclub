import factory

from django.contrib.auth import get_user_model
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("word")
    email = factory.Faker('email')
    password = factory.Faker("password")