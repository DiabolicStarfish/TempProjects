from fibo import fibo

def test_fibo():
    assert fibo(0) == 0
    assert fibo(1) == 1
    assert fibo(13) == 233
    assert fibo(11) == 89