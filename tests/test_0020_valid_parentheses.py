import pytest
from solutions.stack._0020_valid_parentheses.solution import Solution

@pytest.mark.parametrize("s,expected", [
    ("(", False),
    ("(]", False),
    ("([)]", False),
    ("()", True),
    ("()[]{}", True),
    ("{[]}", True),
])
def test_valid_parentheses(s, expected):
    assert Solution().isValid(s) == expected
