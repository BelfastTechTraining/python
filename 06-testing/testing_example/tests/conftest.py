import pytest

@pytest.fixture()
def common_config():
    return {"foo":123, "bar": ["baz"]}