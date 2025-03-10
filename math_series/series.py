def fibonacci(n):
  '''
  The fibonacci sequence.

  Args:
    n (int): An index.

  Returns:
    int: Number at that index in the Fibonacci sequence.
  '''
  if n == 1:
    return 1
  if n == 0:
    return 0
  return fibonacci(n - 2) + fibonacci(n - 1)

def lucas(n):
  '''
  The lucas numbers.

  Args:
    n (int): An index.

  Returns:
    int: Number at that index in the lucus numbers sequence.
  '''
  if n == 1:
    return 1
  if n == 0:
    return 2
  return lucas(n - 2) + lucas(n - 1)

def sum_series(n, start1=0, start2=1):
  '''
  Args:
    n (int): An index.
    start1 (int): First value for series.
    start2 (int): Second value for series.

  Returns:
    int: Number at that index in the series.
  '''
  if start1 + start2 == 1:
    return fibonacci(n)
  if start1 + start2 == 3 and start1 != 3 and start2 != 3:
    return lucas(n)
  if n == 0:
    return start1
  if n == 1:
    return start2
  return sum_series(n - 2, start1, start2) + sum_series(n - 1, start1, start2)
