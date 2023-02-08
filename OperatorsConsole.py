Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #operator
>>> #arithmetic operators: + - / * % ** //
>>> #comparison operator
>>> 5 < 10
True
>>> 10> 1000
False
>>> 5 >= 5
True
>>> 10 <= 1000
True
>>> #equality operator
>>> 5 == 10
False
>>> 5 == 5
True
>>> 5 != 5
False
>>> 5 != 10
True
>>> #logical operator
>>> #and or not
>>> #and-
>>> 5 > 10 and 5 < 10
False
>>> 5 > 10 and 5 < 10 and 10 == 10
False
>>> 5 ==5 and 5 < 10
True
>>> #or -atleast 1 condition -> True ->overall ans-True
>>> 5 > 10 or 5 < 10 or 10 == 10
True
>>> #not - True ->false , False - >True
>>> 5 <= 10
True
>>> not 5<=10
False
>>> #Bitwise Operator
>>> #and ->min
>>> #or->max
>>> 10 & 20
0
>>> 10 && 20
SyntaxError: invalid syntax
>>> 10 & 4
0
>>> 10 and 5
5
>>> 10 | 5
15
>>> 10 or 5
10
>>> ~ 10
-11
>>> ~(-11)
10
>>> 25 << 1
50
>>> 25 >> 1
12
>>> 25 << 2
100
>>> #assignment operator
>>> x = 12
>>> x += 1
>>> x
13
>>> x-=3
>>> x
10
>>> x /= 5
>>> x
2.0
>>> x *= 3 # x=x*3
>>> x
6.0
>>> x %= 2
>>> x
0.0
>>> x = 2
>>>  x **= 5
 
SyntaxError: unexpected indent
>>> x **= 5
>>> x
32
>>> x &= 20
>>> x
0
>>> x |= 98
>>> x
98
>>> x <<= 2
>>> x
392
>>> x >>=3
>>> x
49
>>> #Membership operator
>>> vowels = "aeiou"
>>> "z" in vowels
False
>>> "a" in vowels
True
>>> "z" not in vowels
True
>>> #identical operator
>>> x = 2
>>> y = 12
>>> x is y
False
>>> x =2
>>> y=2
>>> x is y
True
>>> x=[1,2,3]
>>> y = [1,2,3]
>>> x is y
False
>>> id(x)
140397325595584
>>> id(y)
140397325597504
>>> x = [1,2,3,4]
>>> y = x
>>> id(x)
140397326086016
>>> id(y)
140397326086016
>>> x is y
True
>>> x = [1,2,3]
>>> y = [1,2,3]
>>> x is y
False
>>>  x==y
 
SyntaxError: unexpected indent
>>> x==y
True
>>> x is y
False
>>> x is not y
True
>>> 