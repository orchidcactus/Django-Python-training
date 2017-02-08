#function that takes a character and returns true if its vowel, false otherwise.

def is_vowel(x):
    if x in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False

ch= raw_input('enter a chracter:', )
print is_vowel(ch)