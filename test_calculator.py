import pytest
from calculator import evaluate

def test_different_symbols():
    with pytest.raises(SyntaxError) as s_error:
        eval('%%$$$')
    assert 'invalid syntax' in str(s_error.value)

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as error:
        evaluate(5/0)
    assert 'division by zero' in str(error.value)

import pytest
from calculator import evaluate

def test_answer():
    assert eval('2*2') == 4