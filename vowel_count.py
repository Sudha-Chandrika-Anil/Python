def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

chk=intput("Enter string")
print(count_vowels(chk))  

