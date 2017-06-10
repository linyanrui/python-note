Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> class int(int):
	def __add__(self, other):
		return int.__sub__(self, other)

	
>>> a = int('5')
>>> a
5
>>> b = int(3)
>>> a + b
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self, other)

	
>>> a = Nint(5)
>>> b = Nint(3)
>>> a + b
8
>>> 1 + b
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(self, other)

	
>>> a = Nint(5)
>>> 3 - a
2
>>> class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(other, self)

	
>>> a = Nint(5)
>>> 3 - a
-2
>>> 
