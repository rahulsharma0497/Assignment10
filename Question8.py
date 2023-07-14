def count_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0

    for char in string:
        if char in consonants:
            count += 1

    return count

# Test cases
print(count_consonants("Hello World"))  # Output: 7
print(count_consonants("OpenAI Chatbot"))  # Output: 10
print(count_consonants("Python"))  # Output: 4
