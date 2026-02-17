from itertools import count

alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
nonvowel = "bcdfghjklmnpqrstvwxyz"
message = ""
with open("secret.txt") as f:
    for line in f:
        num_vowels = 0
        for v in vowel:
            num_vowels += line.count(v)
        letter = alphabet[num_vowels]
        message += letter
        print(message)

