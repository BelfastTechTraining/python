import pytest

@pytest.fixture(scope="session")
def session_scoped():
    print("\nsession_scoped")

@pytest.fixture(scope="module")
def module_scoped():
    print("module_scoped")

@pytest.fixture
def function1(tmpdir):
    print("function1")

@pytest.fixture
def function2(function3):
    print("function2")

@pytest.fixture
def function3():
    print("function3")

def test_foo(function1, module_scoped, function2, session_scoped):
    pass
