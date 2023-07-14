def count_substrings_with_same_ending_and_starting_character(s):
  """
  Returns the count of all contiguous substrings starting and ending with same character in string s.

  Args:
    s: A string.

  Returns:
    The count of all contiguous substrings starting and ending with same character in string s.
  """

  count = 0
  for i in range(len(s)):
    if s[i] == s[0]:
      start = i
      end = i
      while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
      count += end - start - 1
  return count


if __name__ == "__main__":
  s = "abcabc"
  print(count_substrings_with_same_ending_and_starting_character(s))