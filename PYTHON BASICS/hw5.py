# Vowel consonant checking also an alphabet or not

alpha=input("Enter a character:")

vowels={'a','e','i','o','u','A','E','I','O','U'}\

if alpha.isalpha():
    if alpha in vowels:
        print("Entered character is Vowel")
    else:
        print("Entered character is Consonant")
else:
    print("Not an alphabet")