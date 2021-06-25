#Execution time : 0.02s
def reverseWord(s):
    str = ""
    for i in s :
        str = i + str
    return(str)
# Pythonic 

def reverseWord(s):
    return(s[::-1])
