# 在 decorator.py 的例子中，以 function (decorator_func) 當作 decorator。
# 也可以用 class 當作 decorator，詳看以下例子:

class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func
    def __call__(self, *args, **kwargs): # 像是 wrapper_func。
        print('call method exectued this before')
        return self.original_func(*args, **kwargs)

@decorator_class
def display():
    print('display function ran')

display()