def palindrome(str):
    if str==str[::-1]:
        return "Palindrome"
    return "Not Palindrome"

print(palindrome('shweta'))
