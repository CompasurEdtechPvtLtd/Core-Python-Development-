Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "Harsh Vardhan"
>>> #string slicing
>>> #x[starting index : ending index]
>>> x[0:4]
'Hars'
>>> #ending index - n-1
>>> x[0:5]
'Harsh'
>>> x
'Harsh Vardhan'
>>> x[:5]
'Harsh'
>>> x[5:]
' Vardhan'
>>> x[:]
'Harsh Vardhan'
>>> #x[starting:ending:inc/dec]
>>> x[0:5]
'Harsh'
>>> x[0:5:1]
'Harsh'
>>> x[::2]
'HrhVrhn'
>>> #find the reverse of the string
>>> x[12:0:-1]
'nahdraV hsra'
>>> #range - > small to big ->ending range - n-1
>>> #range - > big to small ->ending range - n+1
>>> x[12:-1:-1]
''
>>> x[12::-1]
'nahdraV hsraH'
>>> x
'Harsh Vardhan'
>>> x[::-1]
'nahdraV hsraH'
>>> #string methods
>>> x
'Harsh Vardhan'
>>> x.lower()
'harsh vardhan'
>>> x
'Harsh Vardhan'
>>> x = x.lower()
>>> x
'harsh vardhan'
>>> x.upper()
'HARSH VARDHAN'
>>> "HARSH".casefold()
'harsh'
>>> x
'harsh vardhan'
>>> x = "HaRsH"
>>> x.casefold()
'harsh'
>>> x.swapcase()
'hArSh'
>>> x = "welcome to our python programming class"
>>> x.capitalize()
'Welcome to our python programming class'
>>> x.title()
'Welcome To Our Python Programming Class'
>>> x="Harsh Kumar"
>>> x.replace("Kumar","Vardhan")
'Harsh Vardhan'
>>> x
'Harsh Kumar'
>>> x="Harsh"
>>> x.center(4)
'Harsh'
>>> x.center(5)
'Harsh'
>>> x.center(6)
'Harsh '
>>> x.center(7)
' Harsh '
>>> x.center(20)
'       Harsh        '
>>> x.center(20,"*")
'*******Harsh********'
>>> x.center(20,"/")
'///////Harsh////////'
>>> x.center(20,"@")
'@@@@@@@Harsh@@@@@@@@'
>>> x = "aaabbbcccdddddddd"
>>> x.replace('a','x')
'xxxbbbcccdddddddd'
>>> x.replace('a','x',2)
'xxabbbcccdddddddd'
>>> x='       Harsh        '
>>> x.lstrip()
'Harsh        '
>>> x.rstrip()
'       Harsh'
>>> x.strip()
'Harsh'
>>> x ='@@@@@@@Harsh@@@@@@@@'
>>> x.strip()
'@@@@@@@Harsh@@@@@@@@'
>>> x.strip("@")
'Harsh'
>>> x = "@@@H@rsh@@@"
>>> x.strip("@")
'H@rsh'
>>> x
'@@@H@rsh@@@'
>>> len(x)
11
>>> x.zfill(10)
'@@@H@rsh@@@'
>>> x.zfill(11)
'@@@H@rsh@@@'
>>> x.zfill(50)
'000000000000000000000000000000000000000@@@H@rsh@@@'
>>> x.zfill(15)
'0000@@@H@rsh@@@'
>>> x = "Harsh"
>>> x.startswith("x")
False
>>> x.startswith("h")
False
>>> x.startswith("H")
True
>>> x.endswith("h")
True
>>> x
'Harsh'
>>> x.isdigit()
False
>>> x="123"
>>> x.isdigit()
True
>>> x
'123'
>>> x.isalpha()
False
>>> x="1A2B"
>>> x.isalpha()
False
>>> x.isnan()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    x.isnan()
AttributeError: 'str' object has no attribute 'isnan'
>>> x.isalphanumeric()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    x.isalphanumeric()
AttributeError: 'str' object has no attribute 'isalphanumeric'
>>> x.alnum()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    x.alnum()
AttributeError: 'str' object has no attribute 'alnum'
>>> x.isalnum()
True
>>> x
'1A2B'
>>> x="12.566"
>>> x.isdecimal()
False
>>> x = "\u0003"
>>> x.isdecimal()
False
>>> x = "\u0033"
>>> x.isdecimal()
True
>>> #ASCII ->American Standard code for information interchange
>>> #ord-ordinal & chr - character
>>> ord("A")
65
>>> char(70)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    char(70)
NameError: name 'char' is not defined
>>> chr(70)
'F'
>>> chr(100)
'd'
>>> x = "harsh"
>>> y = "vardhan"
>>> x+y
'harshvardhan'
>>> x-y
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> x/y
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    x/y
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> x*y
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'str'
>>> x
'harsh'
>>> x*10
'harshharshharshharshharshharshharshharshharshharsh'
>>> 