Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: /Users/ifeng/Desktop/python学习笔记/1-45-MyTimer-4.py =========
>>> t1 = MyTimer()
>>> t1
not start calculating yet
>>> t1.stop()
tip: please start calculating first
>>> t1.start()
star calculate
>>> t1.start()
star calculate
>>> t1
tip: please stop calculating first
>>> t1.stop()
stop calculating
>>> t1
the total running time is 1minute-31second
>>> 
========= RESTART: /Users/ifeng/Desktop/python学习笔记/1-45-MyTimer-4.py =========
>>> t1 = MyTimer()
>>> t1
not start calculating yet
>>> t1.stop()
tip: please start calculating first
>>> t1.start()
star calculate
>>> t1.stop()
stop calculating
>>> t1
the total running time is 1minute-53second
>>> t2 = MyTimer()
>>> t2.star()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t2.star()
AttributeError: 'MyTimer' object has no attribute 'star'
>>> t2.start()
star calculate
>>> t2.stop()
stop calculating
>>> t2
the total running time is 5second
>>> t1+t2
'the total running time is 1minute-48second'
>>> t1 = MyTimer()
>>> t1.star()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t1.star()
AttributeError: 'MyTimer' object has no attribute 'star'
>>> t1.start()
star calculate
>>> t1.stop()
stop calculating
>>> T1
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    T1
NameError: name 'T1' is not defined
>>> t1
the total running time is 6second
>>> t1 + 2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t1 + 2
  File "/Users/ifeng/Desktop/python学习笔记/1-45-MyTimer-4.py", line 19, in __add__
    result.append(self.lasted[index]+other.lasted[index])
AttributeError: 'int' object has no attribute 'lasted'
>>> t1 +t2
'the total running time is 11second'
>>> class C:
	def __init__(self)"
	
SyntaxError: EOL while scanning string literal
>>> claxx C:
	
SyntaxError: invalid syntax
>>> class C:
	def __init__(self):
		self.x = 'X-man'

		
>>> c = C()
>>> c.x
'X-man'
>>> getattr(c,'x','no this attribute')
'X-man'
>>> getattr(c,'y', 'no this attribute')
'no this attribute'
>>> 
=============================== RESTART: Shell ===============================
>>> class C:
	def __init__(self, size = 10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self, value):
		self.size = value
	def delSize(self):
		del self.size

		
>>> class C:
	def __init__(self, size = 10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self, value):
		self.size = value
	def delSize(self):
		del self.size
	x = property(getSize, setSize, delSize)

	
>>> c = C()
>>> c.x
10
>>> c.x = 12
>>> c.x
12
>>> c.size
12
>>> del c.x
>>> c.size
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c.size
AttributeError: 'C' object has no attribute 'size'
>>> 
=============================== RESTART: Shell ===============================
>>> class C:
	def __getattribute__(self, name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('getattr')
	def __setattr__(self, name, value)
	
SyntaxError: invalid syntax
>>> class C:
	def __getattribute__(self, name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('getattr')
	def __setattr__(self, name, value);
	
SyntaxError: invalid syntax
>>> class C:
	def __getattribute__(self, name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('getattr')
	def __setattr__(self, name, value):
		print('setattr')
		super().__setattr__(name, value)
		def __delattr__(self, name):
			print('delattr')
			super().__delattr__(name)

			
>>> c = C()
>>> c.x
getattribute
getattr
>>> c.x = 1
setattr
>>> c.x
getattribute
1
>>> class C:
	def __getattribute__(self, name):
		print('getattribute')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('getattr')
	def __setattr__(self, name, value):
		print('setattr')
		super().__setattr__(name, value)
	def __delattr__(self, name):
		print('delattr')
		super().__delattr__(name)

		
>>> c = C()
>>> del c.x
delattr
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    del c.x
  File "<pyshell#83>", line 12, in __delattr__
    super().__delattr__(name)
AttributeError: x
>>> c.x
getattribute
getattr
>>> c.x = 1
setattr
>>> c.x
getattribute
1
>>> del c.x
delattr
>>> 
