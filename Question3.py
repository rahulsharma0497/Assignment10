def print_all_subsets(set, index):
  """
  Prints all subsets of set.

  Args:
    set: A string.
    index: The index of the current character in set.

  Returns:
    None.
  """

  if index == len(set):
    print("")
    return
  else:
    print_all_subsets(set, index + 1)
    print(set[index], end="")
    print_all_subsets(set, index + 1)


if __name__ == "__main__":
  set = "abc"
  print_all_subsets(set, 0)