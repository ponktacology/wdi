def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = 0
    for i in range(len(s)):
        if s[i] in vowels:
            result += 1
    return result

def is_equal_weight(s1, s2):
    if count_vowels(s1) != count_vowels(s2):
        return False
    
    as1 = 0
    as2 = 0

    for i in range(len(s1)):
        as1 += ord(s1[i])
    for i in range(len(s2)):
        as2 += ord(s2[i])
    
    return as1 == as2

def wyraz(og, index, s1, s2):
    if is_equal_weight(s1, s2):
        print(s1)
        return True
    if index == len(og):
        return False

    if wyraz(og, index + 1, s1 + og[index], s2):
        return True
    elif wyraz(og, index + 1, s1, s2):
        return True
    return False

print(wyraz("awdawduawdawlawda", 0, "", "exe"))
    



