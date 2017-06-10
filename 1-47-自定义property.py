Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> class MyDecriptor:
	def __get__(self, instance, owner):
		print('getting...', self, instance, owner)
		
	def __set__(self, instance, value):
		print('setting...', self, instance, value)
		
	def __delete__(self, instance):
		print('deleting...', self, instance)

		
>>> class test:
	x = MyDecriptor()

	
>>> test = Test()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    test = Test()
NameError: name 'Test' is not defined
>>> ta = test()
>>> ta.x
getting... <__main__.MyDecriptor object at 0x105591908> <__main__.test object at 0x1055d3470> <class '__main__.test'>
>>> ta
<__main__.test object at 0x1055d3470>
>>> test
<class '__main__.test'>
>>> ta.x = 'X-man'
setting... <__main__.MyDecriptor object at 0x105591908> <__main__.test object at 0x1055d3470> X-man
>>> del ta.x
deleting... <__main__.MyDecriptor object at 0x105591908> <__main__.test object at 0x1055d3470>
>>> 
=============================== RESTART: Shell ===============================
>>> class MyProperty:
	def __init__(self, fget = None, fset = None, fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		
	def __get__(self, instance, owner):
		return self.fget(instance)
	
	def __set__9self, instance, value):
		
SyntaxError: invalid syntax
>>> class MyProperty:
	def __init__(self, fget = None, fset = None, fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		
	def __get__(self, instance, owner):
		return self.fget(instance)
	
	def __set__(self, instance, value):
		self.fset(instance, value)
		
	def __del__(self, instance):
		self.fdel(instance)

		
>>> class C:
	def __init__(self):
		self._x = None
		
	def getX(self):
		return self._x
	
	def setX(self, value):
		self._x = value
	def delX(self):
		del self._x

		
>>> class C:
	def __init__(self):
		self._x = None
		
	def getX(self):
		return self._x
	
	def setX(self, value):
		self._x = value
		
	def delX(self):
		del self._x
		
	x = MyProperty(getX, setX, delX)

	
>>> c =C()
>>> c.x = 'x-man'
>>> c.x
'x-man'
>>> c._x
'x-man'
>>> del c.x
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    del c.x
AttributeError: __delete__
>>> 
