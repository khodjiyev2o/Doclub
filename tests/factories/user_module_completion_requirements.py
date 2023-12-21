import factory
from apps.module.models import UserModuleCompletionRequirements


class UserModuleCompletionRequirementsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModuleCompletionRequirements

    module = factory.SubFactory("tests.factories.module.ModuleFactory")
    user = factory.SubFactory("tests.factories.user.UserFactory")
    is_video_played = factory.Faker('boolean')
    is_files_downloaded = factory.Faker('boolean')
    is_test_passed = factory.Faker('boolean')
