import pytest
from pytest_factoryboy import register

from tests.factories import CourseFactory


register(CourseFactory)


@pytest.fixture()
def new_course(db, course_factory):
    return course_factory.create()
