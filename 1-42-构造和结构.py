Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> class Rectangle:
	def __init__(self,x, y):
		self.x = x
		self.y =y
	def getPeri(self):
		return (self.x+self.y) * 2
	def getArea(self):
		return self.x * self.y

	
>>> 
>>> rect = Rectangle()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    rect = Rectangle()
TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>> rect = Rectanle(3, 4)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    rect = Rectanle(3, 4)
NameError: name 'Rectanle' is not defined
>>> rect = Rectangle(3, 4)
>>> rect.getPeri
<bound method Rectangle.getPeri of <__main__.Rectangle object at 0x1054a0cc0>>
>>> rect.getPeri()
14
>>> rect.getArea()
12
>>> class A:
	def __init__(self):
		return 'A fo A-Cup'

	
>>> a = A()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = A()
TypeError: __init__() should return None, not 'str'
>>> class CapStr(str):
	def __new__(cls,strinng):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> a = Capstr('i love FisnC.com')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a = Capstr('i love FisnC.com')
NameError: name 'Capstr' is not defined
>>> a = CapStr('i love FisnC.com')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a = CapStr('i love FisnC.com')
  File "<pyshell#18>", line 3, in __new__
    string = string.upper()
UnboundLocalError: local variable 'string' referenced before assignment
>>> 
>>> class CapStr(str):
	def __new__(cls,strinng):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> 
=============================== RESTART: Shell ===============================
>>> class CapStr(str):
	def __new__(cls,strinng):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> class CapStr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)

	
>>> a = CapStr('i love FIshC.com')
>>> a
'I LOVE FISHC.COM'
>>> class C:
	def __init__(self):
		print('i am __init__')
	def __del__(self):
		print('i am __del__')

		
>>> c1 = C()
i am __init__
>>> c2 = c1
>>> c3 = c2
>>> del c3
>>> del c2
>>> cel c1
SyntaxError: invalid syntax
>>> del c1
i am __del__
>>> 
