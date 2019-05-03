import pytest
from testing_example import main


def test_product():
    assert main.product(2, 3) == 6

def test_product_invalid_type():
    with pytest.raises(TypeError, match=".*unsupported operand type.*") as excinfo:
        assert main.product(-3, None)