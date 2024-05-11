text = input()

vowel_values = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}
result = 0

for char in text:
    if char in vowel_values:
        result += vowel_values[char]

print(result)