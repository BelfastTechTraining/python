import pytest

def test_shared_fixtures(common_config):
    assert common_config["foo"] == 123