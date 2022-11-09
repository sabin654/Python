char = input("Enter character")


if char.lower() in ('a', 'e', 'i', 'o', 'u'):  
 print(char, "is a Vowel")
 
elif char.upper() in ('A', 'E', 'I', 'O', 'U'): 
 print(char, "is a Vowel")
 
else:
 print(char, "is a Consonant")
