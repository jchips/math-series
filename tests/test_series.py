from math_series.series import fibonacci, lucas, sum_series

def test_fibonnaci_1():
 actual = fibonacci(1)
 expect = 1
 assert actual == expect

def test_fibonnaci_2():
  actual = fibonacci(2)
  expect = 1
  assert actual == expect

def test_fibonnaci_3():
  actual = fibonacci(3)
  expect = 2
  assert actual == expect

def test_fibonnaci_10():
  actual = fibonacci(10)
  expect = 55
  assert actual == expect

def test_lucas_1():
  actual = lucas(1)
  expect = 1
  assert actual == expect

def test_lucas_2():
  actual = lucas(2)
  expect = 3
  assert actual == expect

def test_lucas_3():
  actual = lucas(3)
  expect = 4
  assert actual == expect

def test_lucas_4():
  actual = lucas(4)
  expect = 7
  assert actual == expect

def test_lucas_10():
  actual = lucas(10)
  expect = 123
  assert actual == expect

def test_sum_series_fib_1():
  actual = sum_series(1)
  expect = 1
  assert actual == expect

def test_sum_series_fib_10():
  actual = sum_series(10)
  expect = 55
  assert actual == expect

def test_sum_series_luc_1():
  actual = sum_series(1, 2, 1)
  expect = 1
  assert actual == expect

def test_sum_series_luc_10():
  actual = sum_series(10, 2, 1)
  expect = 123
  assert actual == expect

def test_sum_series_2():
  actual = sum_series(2, 2, 0)
  expect = 2
  assert actual == expect

def test_sum_series_7():
  actual = sum_series(7, 2, 0)
  expect = 16
  assert actual == expect
