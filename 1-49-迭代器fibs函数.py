Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> string = 'FishC'
>>> it = iter(string)
SyntaxError: multiple statements found while compiling a single statement
>>> string = 'fishc'
>>> it = iter(string)
>>> while True:
	try:
		each = next(it)
	except StopIteration:
		break
	print(each)

	
f
i
s
h
c
>>> class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		return self.a

	
>>> fibs = Fibs()
>>> for each in fibs:
	if each < 20:
		print(each)
	else:
		break

	
1
1
2
3
5
8
13
>>> class Fibs:
	def __init__(self,n = 10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.n
			raise StopIteration
		return self.a
	
SyntaxError: invalid syntax
>>> class Fibs:
	def __init__(self,n = 10):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a

	
>>> fibs = Fibs()
>>> for each in fibs:
	pring(each)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    pring(each)
NameError: name 'pring' is not defined
>>> for each in fibs:
	print(each)

	
1
2
3
5
8
>>> fibs = Fibs(100)
>>> for each in fibs:
	print(each)

	
1
1
2
3
5
8
13
21
34
55
89
>>> 
