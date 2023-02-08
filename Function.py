'''
def Temp(c):
    return 5/9*c+32



#res = Temp(32)



x = [23,32,45,34,38,32.5,33.99]

res = list(map(Temp,x))
print(res)


def Even(x):
    if x%2==0:
        return True
    else:
        return False

x = [23,328,45,34,38,32,33]
res=list(filter(Even,x))
print(res)
'''
'''
x = lambda c : 5/9*c+32
print(x(74))
'''
y = lambda x:True if x%2==0 else False
print(y(65))
