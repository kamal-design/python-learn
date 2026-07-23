"""Short summary: contains testcase notes or examples."""
from code_logic import divide

def test_divide_regular():
    """Tests that dividing two regular numbers returns the correct float result."""
    try:
        assert divide(6,2) == 3.0
        print("Test Case PASSED ✅")
    except AssertionError:
        print("Test Case FAILED ❌")

test_divide_regular()