def pangram(str):
    a='abcdefghijklmnopqrstuvwxyz'
    for x in a:
        if x not in str and chr(ord(x)+32) not in str and chr(ord(x)-32) not in str:
            return "Not Pangram"
    else:
        return "Pangram"

print(pangram('The quick brown fox jumps over the lazy DOG'))