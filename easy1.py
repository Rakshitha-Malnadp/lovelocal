# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal 
# substring consisting of non-space characters only.

def easy1(string):
    return len(string.split()[-1])

string=input()
answer=easy1(string)
print(answer)