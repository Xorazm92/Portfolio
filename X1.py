def tozala(s):
    yangi = []
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in "({[":
            yangi.append(char)
        else:
            if not yangi or matching[yangi[-1]] != char:
                return False
            yangi.pop()
    
    return len(yangi) == 0

s = '(()())'
print(tozala(s)) 

s = '[[][[['
print(tozala(s))

s = '[[{}()]]'
print(tozala(s)) 

s = '[[(}]]'
print(tozala(s)) 

