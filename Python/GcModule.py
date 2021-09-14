# gc 是 Python 底层内存管理机制（自动垃圾回收装置）的接口。
# 模块中包含控制回收装置行为和检查暴露到系统中对象的函数，还有挂起收集，禁止引用循环和释放的函数。

# 追踪引用
# gc 可以收集对象间的引用关系，用于寻找复杂数据结构中的循环。如果某数据结构有自己的循环，我们可以自定义代码来检测它的属性
import pprint
'''
该pprint模块提供了以可以用作解释器输入的形式“漂亮地”打印任意Python数据结构的能力。
如果格式化结构包含不是基本Python类型的对象，则该表示可能无法加载。如果包含诸如文件，套接字，类或实例的对象，以及许多其他不能表示为Python常量的内置对象，则可能会出现这种情况。
'''

import queue

import gc
'''
追踪引用
gc 可以收集对象间的引用关系，用于寻找复杂数据结构中的循环。

强制垃圾回收
    尽管垃圾回收器在解释器运行程序时会自动进行工作，我们可能还是要在某些时候手动运行一下，特别是有大量对象需要释放，或者并没有太多需要处理所以此时运行垃圾回收器不会对性能有所损害。我们可以用 collect() 来触发一次回收


回收阈值和代数
运行时，垃圾收集器维护着 3 个对象列表，其中一个是对 「代」的追踪。当对象在每次「代」的检查中，它们要么被回收要么进入下一代，反复如此直到最终无法被回收。

回收器的检查会基于不同的对象分配与释放频率而触发。当分配的数量减去释放的数量大于当前代指定的阈值时，垃圾回收器就会运行。当前的阈值是多少可以通过 get_threshold() 知道。

'''


class Graph:
    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next
        print('Linking nodes {}.next = {}'.format(self, next))

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name)

'''
without __repr__:
    Linking nodes <__main__.Graph object at 0x7fe482c390f0>.next = <__main__.Graph object at 0x7fe482c390b8>
    Linking nodes <__main__.Graph object at 0x7fe482c390b8>.next = <__main__.Graph object at 0x7fe482c3f3c8>
    Linking nodes <__main__.Graph object at 0x7fe482c3f3c8>.next = <__main__.Graph object at 0x7fe482c390f0>

with __repr__:
    Linking nodes Graph(one).next = Graph(two)
    Linking nodes Graph(two).next = Graph(three)
    Linking nodes Graph(three).next = Graph(one)
原理：
    print(person) # <__main__.Person object at 0x0025A6A0>
    print(person.__repr__) # <method-wrapper '__repr__' of Person object at 0x0025A6A0>
    输出实例化的Person类，返回的是一个在内存中的对象，实际上输出的是person对象上__repr__方法的返回值
因此：当直接打印类的实例化对象时，系统将会输出对象的自我描述信息，用来告诉外界对象具有的状态信息，重写了__repr__，打印person实例时，就可以返回类的 ”自我描述“ 的信息。
'''

# 构造一个引用循环。
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# 从此模块的命名空间中删除这些节点的引用。
one = two = three = None


print('\n three refers to:')
# get_referents() 函数可以根据输入的参数显示对象的 引用目标。
for r in gc.get_referents(two):
    pprint.pprint(r)


'''
本例中，这个引用循环被直接清理了，因为除了 Graph 之外，没有其他的引用指向它们了。 
collect() 会返回它所找到的「无法再访问」对象的数量。例子中显示的是 6，因为有 3 个对象以及它们的实例属性字典。
'''
# 显示出垃圾回收的结果。
for i in range(2):
    print('\nCollecting {} ...'.format(i))
    n = gc.collect(2)
    print('Unreachable objects:', n)
    print('Remaining Garbage:', end=' ')
    pprint.pprint(gc.garbage)