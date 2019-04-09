import random
def num_vowels(word):
    vowels=["a", "e", "i", "o", "u"]
    vowel_count=0
    for x in word:
        if x in vowels:
            vowel_count+=1
    return vowel_count
