import pytest
from solutions.s01_stack.lc_0020_valid_parentheses import Solution

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
