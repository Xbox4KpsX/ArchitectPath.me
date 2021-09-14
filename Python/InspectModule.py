


import inspect
'''
inspect模块提供实时了解对象的函数，包括模块、类、实例、函数和方法；
此模块中的函数可用于检索函数的原始源代码，查看堆栈上方法的参数，并提取有助于生成源代码库文档的信息。

https://learnku.com/docs/pymotw/inspect-inspect-live-objects/3490

此模块中的函数可用于检索函数的原始源代码，查看堆栈上方法的参数，并提取有助于生成源代码库文档的信息。

审查模块
审查类
审查实例
文档字符串
检索来源
    如果模块包含可用的 .py 文件，则可以使用 getsource() 和 getsourcelines() 来检索类或方法的原始源代码。
方法和函数签名
类层次结构
方法解析顺序
堆栈和帧
'''


def module_level_function(arg1, arg2='default', *args, **kwargs):
    """该函数在模块中声明"""
    local_variable = arg1 * 2
    return local_variable

class A(object):
    """The A class."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Returns the name of the instance."
        return self.name

instance_of_a = A('sample_instance')

class B(A):
    """This is the B class.
    It is derived from A.
    """

    # 此方法不是 A 的一部分。
    def do_something(self):
        """Does some work"""

    def get_name(self):
        "Overrides version from A"
        return 'B(' + self.name + ')'


for name, data in inspect.getmembers(A):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))

# 方法和函数签名：对可调用的参数进行完整的规范，包括默认值。 
# signature() 函数返回一个 Signature 实例，其中包含有关该函数参数的信息。
# 函数的 Signature 可以被装饰器或其他函数用来验证输入，提供不同的默认值等。
# 提供默认值：bind() 和 bind_partial() 方法提供了处理映射所必需的逻辑。 它们返回一个 BoundArguments 实例，该实例填充了与指定函数的参数名称相关联的参数。

# Pass follow_wrapped=False to get a signature of obj without unwrapping its __wrapped__ chain.
sig = inspect.signature(module_level_function, follow_wrapped=False)
print("sig = \n {} \n".format(sig))
print('sig.parameters = \n {} \n'.format(sig.parameters))
print('\nmodule_level_function{}'.format(sig))

# 类层次结构
# inspect 包括两种直接使用类层次结构的方法。 第一个是 getclasstree() ，它根据给定的类及其基类创建一个类似树的数据结构。 返回的列表中的每个元素都是带有类及其基类的元组，或者是包含子类元组的另一个列表。




