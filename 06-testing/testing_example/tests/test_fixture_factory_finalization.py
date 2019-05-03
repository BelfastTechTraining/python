import pytest

@pytest.fixture
def make_people():
    from testing_example import Person
    created_people= []

    def _make_person(name, age):
        person = Person(name=name, age=age)
        created_people.append(person)
        return person

    yield _make_person

    for person in created_people:
        person.die()

def test_fixture_factory_teardown(make_people):
    tom = make_people("Tom", 20)
    dick = make_people("Dick", 30)
    harry = make_people("Harry", 40)
    assert tom.age == 20
    assert dick.age == 30
    assert harry.age == 40
    print("\nALL IS WELL, TIME TO DIE")
