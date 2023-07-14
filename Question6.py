def tower_of_hanoi(n, source, aux, dest):
  """
  Prints the steps of discs movement and returns the total moves.

  Args:
    n: The number of discs.
    source: The source rod.
    aux: The auxiliary rod.
    dest: The destination rod.

  Returns:
    The total moves.
  """

  if n == 1:
    print(f"Move disk {n} from {source} to {dest}")
    return 1
  else:
    moves = tower_of_hanoi(n - 1, source, dest, aux)
    print(f"Move disk {n} from {source} to {dest}")
    moves += tower_of_hanoi(n - 1, aux, source, dest)
    return moves + 2


if __name__ == "__main__":
  n = 3
  moves = tower_of_hanoi(n, 1, 2, 3)
  print(f"Total moves: {moves}")