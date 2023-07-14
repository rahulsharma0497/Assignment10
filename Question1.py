def is_power_of_three(n):
  """
  Returns true if n is a power of three, otherwise false.

  Args:
    n: An integer.

  Returns:
    True if n is a power of three, otherwise false.
  """

  if n <= 0:
    return False
  while n % 3 == 0:
    n = n / 3
  return n == 1


if __name__ == "__main__":
  n = 27
  print(is_power_of_three(n))