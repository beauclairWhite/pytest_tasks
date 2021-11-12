import pytest
from calculator import evaluate

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as error:
        evaluate(5/0)
    assert 'division by zero' in str(error.value)

