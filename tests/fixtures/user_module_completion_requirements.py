import pytest
from tests.factories import UserFactory, ModuleFactory, UserModuleCompletionRequirementsFactory


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def module(db):
    return ModuleFactory()


@pytest.fixture
def user_module_completion_requirements(db, user, module):
    return UserModuleCompletionRequirementsFactory(user=user, module=module)
