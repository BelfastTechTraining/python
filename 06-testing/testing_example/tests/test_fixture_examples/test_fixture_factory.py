import pytest

@pytest.fixture
def make_person():
    from testing_example import Person
    def _make_person(name, age):
        person = Person(name=name, age=age)
        return person
    return _make_person

def test_fixture_factory(make_person):
    tom = make_person("Tom", 20)
    dick = make_person("Dick", 30)
    harry = make_person("Harry", 40)
    assert tom.age == 20
    assert dick.age == 30
    assert harry.age == 40