def last_remaining_number(n):
  """
  Returns the last number that remains in arr.

  Args:
    n: An integer.

  Returns:
    The last number that remains in arr.
  """

  arr = list(range(1, n + 1))
  while len(arr) > 1:
    if len(arr) % 2 == 1:
      arr.pop(0)
    else:
      arr = arr[1::2]
  return arr[0]


if __name__ == "__main__":
  n = 10
  print(last_remaining_number(n))