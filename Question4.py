def length_of_string(s, index):
  """
  Returns the length of string s.

  Args:
    s: A string.
    index: The index of the current character in s.

  Returns:
    The length of string s.
  """

  if index == len(s):
    return 0
  else:
    return 1 + length_of_string(s, index + 1)


if __name__ == "__main__":
  s = "abc"
  print(length_of_string(s, 0))