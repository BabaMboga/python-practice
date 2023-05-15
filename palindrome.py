#William
characters = str(input("Insert letter or number you wish to check as a palindrome: "))
strcharacters = characters.casefold()

rev = reversed(characters)

def checkPalindrome(characters):
    if list(characters) == list(rev):
        print("THIS IS A PALINDROME")
    else:
        print("THIS IS NOT A PALINDROME") 

checkPalindrome(characters)