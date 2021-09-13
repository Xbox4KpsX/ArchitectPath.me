# 在程序内使用trace模块对象，在运行单个函数或运行某个需要追踪的Python命令前，trace可以设置fixture和其他依赖
import trace

# https://learnku.com/docs/pymotw/trace-follow-program-flow/3467
# usage: python -m trace --trace --count TraceModule.py
# --trace   会将所有执行到的声明打印出来
# --count   生成代码覆盖率报告信息，告诉我们哪些代码调用了哪些没用
# --report  只要覆盖信息在.cover中记录，就可以使用该选项来生成报告
# --listfuncs  列出函数调用关系

def recurse(level):
    print('recurse({})'.format(level))
    if level:
        recurse(level - 1)

def not_called():
    print('This function is never called.')

tracer = trace.Trace(count=False, trace=True)

results = tracer.results()
results.write_results(summary=True, coverdir='.')
def main():
    print('This is the main program.')
     #recurse(2)
    # runfunc() 方法接受任意的位置和关键字参数，在 tracer 调用时会将他们传递给函数。
    tracer.runfunc(recurse, 2)
   
if __name__ == '__main__':
    main()

