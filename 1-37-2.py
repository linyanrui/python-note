Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> edward = ['Edward Gumby',42]
>>> john = ['john smith',50]
>>> database = [edward , john]
>>> database
[['Edward Gumby', 42], ['john smith', 50]]
>>> greeting = 'hello'
>>> greeting[0]
'h'
>>> greeting[-1]
'o'
>>> 'hello'[1]
'e'
>>> fourth = input('year:')[3]
year:2005
>>> fourth
'5'
>>> list[]
SyntaxError: invalid syntax
>>> list[]:
	
SyntaxError: invalid syntax
>>> list = []
>>> class MyList(list):
	pass

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    class MyList(list):
TypeError: list() takes at most 1 argument (3 given)
>>> list1 = [1,2]
>>> list1
[1, 2]
>>> class MyList(list1)
SyntaxError: invalid syntax
>>> class MyList(list1):
	pass

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    class MyList(list1):
TypeError: list() takes at most 1 argument (3 given)
>>> class MyList(list()):
	pass

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    class MyList(list()):
TypeError: 'list' object is not callable
>>> class MyList(list1):
	pass

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    class MyList(list1):
TypeError: list() takes at most 1 argument (3 given)
>>> class A:
	def fun(self):
		print('i am xiaoa')

		
>>> class B:
	def fun(self):
		print('i an xiaob')

		
>>> a = A()
>>> b = B()
>>> a.fun()
i am xiaoa
>>> b.fun()
i an xiaob
>>> 
