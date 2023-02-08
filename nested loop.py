#nested loop
"""
for i in range(1,4):
    for j in range(1,4):
        print(i,j)



for i in range(1,4):
    for j in range(0,i):
        print(i,j)


*
**
***
****
*****
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()#nextline

*****
****
***
**
*

for i in reversed(range(1,6)):
    for j in range(i):
        print("*",end="")
    print()#nextline

1
22
333
4444
55555

for i in (range(1,6)):
    for j in range(i):
        print(i,end="")
    print()#nextline

1
12
123
1234
12345

for i in (range(1,6)):
    for j in range(i):
        print(j+1,end="")
    print()#nextline

1
23
456
78910
"
x=1
for i in (range(1,6)):
    for j in range(i):
        print(x,end="")
        x=x+1
    print()#nextline

    *
   **
  ***
 ****
*****
"""

for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(i):
        print("*",end="")
    print()
        
