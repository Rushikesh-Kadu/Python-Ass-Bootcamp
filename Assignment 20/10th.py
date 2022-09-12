def anagram(a,b):
    l=[0 for x in a if x not in b]
    if len(l)>0:
      return "Not Anagram"
    else:
      return "Anagram"
        
print(anagram('silent','listen'))