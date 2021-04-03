import pytest

from .homework import average

@pytest.fixture(params = [
    (5\n, 1 2 3 4 5),
])
def params(request):
    return request.param

def test_d_fibonacci(params):
    N, As, expected = params
    assert average(N, As) == expected
