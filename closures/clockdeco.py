import time

def clock(func):
    print("正在初始化clocked")
    def clocked(*args):
        print("正在调用clocked")
        t0 = time.perf_counter()
        print("马上调用被包装函数")
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name , arg_str, result))
        return result
    print("clocked创建完毕，已经将被包装函数放入clocked")
    return clocked