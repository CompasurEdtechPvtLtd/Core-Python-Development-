#Recursive Fn

def F(x):
    #base case
    if x>10:
        return
    
    print(x)
    F(x+1)

def power(a,b):
    if b ==0:
        return 1

    return a*power(a,b-1)

res=power(5,5)
print(res)
