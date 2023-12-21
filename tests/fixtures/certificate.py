import pytest
from pytest_factoryboy import register

from tests.factories import CertificateFactory


register(CertificateFactory)


@pytest.fixture()
def new_certificate(db, certificate_factory):
    return certificate_factory.create()
