import pytest
from calculator import evaluate

def test_different_symbols():
    with pytest.raises(SyntaxError) as s_error:
        eval('%%$$$')
    assert 'invalid syntax' in str(s_error.value)
