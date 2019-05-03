import pytest
from testing_example import Person

def setup_module(self):
    print("\nMODULE SETUP")

def teardown_module(self):
    print("\nMODULE_TEARDOWN")

def test_can_vote():
    assert 2*3 == 6

