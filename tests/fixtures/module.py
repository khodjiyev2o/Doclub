import pytest
from pytest_factoryboy import register

from tests.factories import ModuleFactory


register(ModuleFactory)


@pytest.fixture()
def new_module(db, module_factory):
    return module_factory.create()
