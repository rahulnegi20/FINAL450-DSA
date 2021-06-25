# exe time : 0.01s
def doUnion(self,a,n,b,m):
    new = []
    a.sort()
    b.sort()
    new = []

    for i in a :
        if i not in new:
            new.append(i)
    for i in b :
        if i not in new:
            new.append(i)
    return(len(new))
  
  #pythonic way 
  # exe time : 0.02s
def doUnion(self,a,n,b,m):
  return len(set(a+b))

# link : https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
