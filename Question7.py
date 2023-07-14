def permutations(str, left, right):
    if left == right:
        print(''.join(str))
    else:
        for i in range(left, right + 1):
            # Swapping characters
            str[left], str[i] = str[i], str[left]
            permutations(str, left + 1, right)
            # Reverting the swap
            str[left], str[i] = str[i], str[left]

# Main function
def print_permutations(str):
    n = len(str)
    str_list = list(str)
    permutations(str_list, 0, n - 1)

# Test cases
print_permutations("cd")
print_permutations("abb")
