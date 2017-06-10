Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> class A:
	pass

>>> class B:
	pass

>>> issubclass(B, A)
False
>>> class B(A):
	pass

>>> issubclass(B, A)
True
>>> issubclass(B,B)
True
>>> issubclass(B, object)
True
>>> b = B()
>>> isinstance(b,B)
True
>>> isinstance(B,B)
False
>>> isinstance(b,A)
True
>>> isinstance(1,A)
False
>>> isinstance(b,b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    isinstance(b,b)
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> 
=============================== RESTART: Shell ===============================
>>> class C:
	def __init__(self, x= 0):
		self.x = x

		
>>> c1 = C()
>>> hasattr(c1, 'x')	#check the attribute
True
>>> getattr(c1,'x')	#get the value of attribute
0
>>> getattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    getattr(c1,'y')
AttributeError: 'C' object has no attribute 'y'
>>> getattr(c1, 'y','don\'t exist this attribute')
"don't exist this attribute"
>>> "don't exist this attribute"
"don't exist this attribute"
>>> 
>>> setattr(c1,'y','FishC')	#set the value of attribute
>>> 				#or just set a new attribute
>>> getattr(c1,'y','don\'t exist this attribute')
'FishC'
>>> delattr(c1,'y')	#del the attribute
>>> delattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    delattr(c1,'y')
AttributeError: y
>>> 
=============================== RESTART: Shell ===============================
>>> class C:
	    def __init__(self, size=10):
		self.size = size
	    def getSize(self):
		return self.size
	    def setSize(self,value):
		self.size = value
	    def delSize(self):
		del self.size
	    x = property(getSize,setSize,delSize)
	    
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class C:
	def __init__(self, size=10):
        self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
	        self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> class C:
	def __init__(self, size=10):
	        self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
	        self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)

	
>>> c1 = C()
>>> c1.getSize()
10
>>> c1.x
10
>>> c1.x = 18
>>> c1.x
18
>>> c1.size
18
>>> C.size
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    C.size
AttributeError: type object 'C' has no attribute 'size'
>>> c1.getSize()
18
>>> del c1.x
>>> c1.size
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c1.size
AttributeError: 'C' object has no attribute 'size'
>>> 
