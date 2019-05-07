import pytest

@pytest.fixture
def kid():
    from testing_example import Person
    return Person("baby jim", 2)

@pytest.fixture
def adult():
    from testing_example import Person
    return Person("old-man river", 200)

def test_kids_cant_vote(kid):    
    assert kid.can_vote() == False

def test_adult_vote(adult):    
    assert adult.can_vote() == True