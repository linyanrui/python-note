Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
class Turtle:# python 中的类名约定以大写字母开头
  """关于类的一个简单例子"""
  # 属性
  color = 'green'
  weight = 10
  legs = 4
  shell = True
  mouth = '大嘴'

  # 方法
  def climb(self)：
    print("我正在很努力的向前爬......")

  def run(self):
    print("我正在飞快的向前跑......")

  def bite(self):
    print("咬死你咬死你！！")

  def eat(self):
    print("有得吃，真满足^_^")

  def sleep(self):
    print("困了，睡了，晚安，Zzzz")
