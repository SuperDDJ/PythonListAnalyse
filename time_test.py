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