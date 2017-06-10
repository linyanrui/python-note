Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> type(len)
<class 'builtin_function_or_method'>
>>> type(dir)
<class 'builtin_function_or_method'>
>>> type(int)
<class 'type'>
>>> type(list)
<class 'type'>
>>> class C:
	pass

>>> type(C)
<class 'type'>
>>> a = int('123')
>>> a
123
>>> b = int('456')
>>> b
456
>>> a +b
579
>>> class New_int(int):
	def __add__(self, other):
		return int.__sub__(self, other)
	def __sub__(self, other):
		return int.__add__(self, other)

	
>>> a = New_int(3)
>>> b = New_int(5)
>>> a +b
-2
>>> a - b
8
>>> class Try_int(int):
	def __add__9self,other):
		
SyntaxError: invalid syntax
>>> class Try_int(int):
	def __add__(self, other):
		return self + other
	def __sub__(self, other):
		return self - other

	
>>> a = Try_iint(3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a = Try_iint(3)
NameError: name 'Try_iint' is not defined
>>> a = Try_int(3)
>>> b = Try_int(5)
>>> a + b
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a + b
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
  File "<pyshell#31>", line 3, in __add__
    return self + other
RecursionError: maximum recursion depth exceeded
>>> class Try_int(int):
	def __add__(self, other):
		return int(self) + int(other)
	def __sub__(self, other):
		return int(self) - int(other)

	
>>> a = Try_int(3)
>>> b = Try_int(4)
>>> a + b
7
>>> a - b
-1
>>> class Try_int(int):
	def __add__(self, other):
		a = self, b = other
		return a + b
	def __sub__(self, other):
		a = self, b = other
		return a - b

	
>>> a = Try_int(3)
>>> b = Try_int(4)
>>> a + b
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a + b
  File "<pyshell#43>", line 3, in __add__
    a = self, b = other
TypeError: 'Try_int' object is not iterable
>>> class Try_int(int):
	def __add__(self, other):
		a.self = self
		b.other = other
		return a.self + b.other
	def __sub__(self, other):
		a.self = self
		b.other = other
		return a.self - b.other

	
>>> a = Try_int(3)
>>> b = Try_int(4)
>>> a + b
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a + b
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
C  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
  File "<pyshell#48>", line 5, in __add__
    return a.self + b.other
RecursionError: maximum recursion depth exceeded
>>> 
