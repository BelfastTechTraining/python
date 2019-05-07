import pytest
from testing_example import Person

@pytest.fixture(scope="module",
                params=[("tom",10), ("dick",20), ("harry",30)])
def person(request):
    person = Person(name=request.param[0], age=request.param[1])
    yield person
    person.die()


def test_fixture_params(person):
    assert type(person.name) == str
