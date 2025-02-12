import numpy as np
import actiontoy


def test_dot():
    vec1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    vec2 = [5.0, 4.0, 3.0, 2.0, 1.0]
    expected = np.dot(vec1, vec2)
    result = actiontoy.dot(vec1, vec2)
    assert np.isclose(result, expected), f"Expected {expected}, got {result}"


def test_dot_length_mismatch():
    vec1 = [1.0, 2.0]
    vec2 = [1.0, 2.0, 3.0]
    try:
        actiontoy.dot(vec1, vec2)
    except ValueError as e:
        assert str(e) == "Vectors must be of the same length"

if __name__ == '__main__':
    test_dot()
    test_dot_length_mismatch()
