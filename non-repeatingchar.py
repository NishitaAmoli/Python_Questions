# Problem:- Return the index of the first non-repeating character in a string. If none exists, return -1.
# Input:- leetcode
#Output:- l

def nonRep(s):
    n = len(s)
    for i in range(n):
        found = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]
    return '$'


s = "leetcode"
print(nonRep(s)) 
