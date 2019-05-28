# PythonListAnalyse
Python列表类型性能测试以及内置字典操作的时间复杂度


### timeit模块


timeit模块可以用来测试一小段Python代码的执行速度。

`class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)`

Timer是测量小段代码执行速度的类。
stmt参数是要测试的代码语句（statment）；
setup参数是运行代码时需要的设置；
timer参数是一个定时器函数，与平台有关。

**timeit.Timer.timeit(number=1000000)**

Timer类中测试语句执行速度的对象方法。number参数是测试代码时的测试次数，默认为1000000次。方法返回执行代码的平均耗时，一个float类型的秒数。

### List的操作测试
```python
import timeit

def test1():
	'''
		通过append方法添加数据
	'''
    li = []
    for i  in range(10000):
        li.append(i)

def test5():
	'''
		通过insert方法添加数据
	'''
    li = []
    for i in range(10000):
        li.insert(0,i)


def test2():
	'''
		通过列表相加添加数据
	'''
    li = []
    for i in range(10000):
        li = li + [i]

def test3():
	'''
		通过推导式添加数据
	'''
    li = [i for i in range(10000)]

def test4():
	'''
		通过list方法添加数据
	'''
    li = list(range(10000))



'''
    因为timeit测试是另外开一个模块测试，所以第二参数中，需要导入要测试函数
    当前模块的模块名称为= __main__
'''
timer1 = timeit.Timer('test1()','from __main__ import test1')
timer5 = timeit.Timer('test5()','from __main__ import test5')
timer2 = timeit.Timer('test2()','from __main__ import test2')
timer3 = timeit.Timer('test3()','from __main__ import test3')
timer4 = timeit.Timer('test4()','from __main__ import test4')

# 测试100次
print('append :%f'%timer1.timeit(number=100))
print('insert :%f'%timer5.timeit(number=100))
print('[]+[] :%f'%timer2.timeit(number=100))
print('[i for] :%f'%timer3.timeit(number=100))
print('list() :%f'%timer4.timeit(number=100))


''' 输出
append :0.171303
insert :2.461631
[]+[] :15.466849
[i for] :0.049168
list() :0.029723
'''
```

### 输出结果：
```python
append :0.171303
insert :2.461631
[]+[] :15.466849
[i for] :0.049168
list() :0.029723
```
### 结论
来个列表相加[] + []操作是非常耗费时间
insert操作比较耗费时间

### pop测试
```python
x = range(2000000)
pop_zero = Timer("x.pop(0)","from __main__ import x")
print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
x = range(2000000)
pop_end = Timer("x.pop()","from __main__ import x")
print("pop_end ",pop_end.timeit(number=1000), "seconds")

# ('pop_zero ', 1.9101738929748535, 'seconds')
# ('pop_end ', 0.00023603439331054688, 'seconds')
```

**测试pop操作：从结果可以看出，pop最后一个元素的效率远远高于pop第一个元素**

### list内置操作的时间复杂度

| 操作 | 时间复杂度 | 描述 |
| --- | --- | --- |
| index[] | O(1) | index[索引] 查找操作 |
| index赋值 | O(1) |index[索引] = 值   赋值操作  |
| append | O(1)） | append追加操作 |
| pop() | O(1) | pop()方法操作的 |
| pop(i) | O(n) | n为操作list的size |
| insert(i，item) | O(n) | n为list的size |
| del操作 | O(n) | n为list的size |
| iteration | O(n) | n为list的size. 遍历操作 |
|  contains| O(n)  | n为list的size |

### dict内置操作的时间复杂度

| 操作 | 时间复杂度 | 描述 |
| --- | --- | --- |
| copy | O(n) |浅拷贝操作  n为dict的size |
| get item | O(1) | 获取字典值  |
| set item | O(1)） | 这是字典值 |
| delete item | O(1) | 删除字典值 |
| iteration | O(n) | n为dictt的size. 遍历操作 |
|  contains| O(1))  | n为list的size |
