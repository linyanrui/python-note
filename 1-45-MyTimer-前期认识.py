Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> t1 = MyTimer()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t1 = MyTimer()
NameError: name 'MyTimer' is not defined
>>> MyTimer()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    MyTimer()
NameError: name 'MyTimer' is not defined
>>> time
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    time
NameError: name 'time' is not defined
>>> import time:
	
SyntaxError: invalid syntax
>>> import time
>>> t1 = MyTimer()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t1 = MyTimer()
NameError: name 'MyTimer' is not defined
>>> class A():
	def __str__(self):
		return 'your are hansome'

	
>>> a = A()
>>> print(a)
your are hansome
>>> a
<__main__.A object at 0x1054a0be0>
>>> class B():
	def __repr__(self):
		return 'you are hansome"
	
SyntaxError: EOL while scanning string literal
>>> class B():
	def __repr__(self):
		return 'you are hansome'

	
>>> b = B()
>>> B
<class '__main__.B'>
>>> print(b)
you are hansome
>>> b
you are hansome
>>> a
<__main__.A object at 0x1054a0be0>
>>> 
