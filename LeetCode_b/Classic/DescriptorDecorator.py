# -*- coding:UTF-8 -*-

# 带参数 函数装饰器
def log(header, footer):  # 相当于在无参装饰器外套一层参数
    def log_to_return(fun):  # 这里接受被装饰的函数
        def return_fun(*args, **kargs):
            print(header)
            fun(*args, **kargs)
            print(footer)

        return return_fun

    return log_to_return



# 带参数 类型装饰器
def flyable(message):
    def flyable_to_return(cls):
        def fly(self):
            print(message)

        cls.fly = fly  # 类属性也可以动态修改
        return cls

    return flyable_to_return


# say(meaasge) ==> log(parms)(say)(message)
@log('日志输出开始', '结束日志输出')
def say(message):
    print(message)


# 定义一个非数据描述符
class myStaticObject(object):
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        print('call myStaticObject __get__')
        return self.fun


# 无参的函数装饰器，返回的是非数据描述符对象
def my_static_method(fun):
    return myStaticObject(fun)


# 定义一个非数据描述符
class myClassObject(object):
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        print('call myClassObject __get__')

        def class_method(*args, **kargs):
            return self.fun(owner, *args, **kargs)

        return class_method


# 无参的函数装饰器，返回的是非数据描述符对象
def my_class_method(fun):
    return myClassObject(fun)


# 非数据描述符
class des1(object):
    def __init__(self, name=None):
        self.__name = name

    def __get__(self, obj, typ=None):
        print('call des1.__get__')
        return self.__name


# 数据描述符
class des2(object):
    def __init__(self, name=None):
        self.__name = name

    def __get__(self, obj, typ=None):
        print('call des2.__get__')
        return self.__name

    def __set__(self, obj, val):
        print('call des2.__set__,val is %s' % (val))
        self.__name = val


# 测试类
@flyable("这是一个测试类")
class test(object):
    def __init__(self, name='test', age=0, sex='man'):
        self.__name = name
        self.__age = age
        self.__sex = sex

    # ---------------------覆盖默认的内建方法
    def __getattribute__(self, name):
        print("start call __getattribute__")
        return super(test, self).__getattribute__(name)

    def __setattr__(self, name, value):
        print("before __setattr__")
        super(test, self).__setattr__(name, value)
        print("after __setattr__")

    def __getattr__(self, attr):
        print("start call __getattr__")
        return attr
        # 此处可以使用getattr()内建函数对包装对象进行授权

    def __str__(self):
        return str('name is %s,age is %d,sex is %s' % (self.__name, self.__age, self.__sex))

    __repr__ = __str__
    # -----------------------
    d1 = des1('chenyang')  # 非数据描述符，可以被实例属性覆盖
    d2 = des2('pengmingyao')  # 数据描述符，不能被实例属性覆盖

    def d3(self):  # 普通函数，为了验证函数(包括函数、静态/类方法)都是非数据描述符，可悲实例属性覆盖
        print('i am a function')

    # ------------------------
    def get_name(self):
        print('call test.get_name')
        return self.__name

    def set_name(self, val):
        print('call test.set_name')
        self.__name = val

    name_proxy = property(get_name, set_name)  # 数据描述符，不能被实例属性覆盖，property本身就是一个描述符类

    def get_age(self):
        print('call test.get_age')
        return self.__age

    age_proxy = property(get_age)  # 非数据描述符，但是也不能被实例属性覆盖

    # ----------------------
    @property
    def sex_proxy(self):
        print("call get sex")
        return self.__sex

    @sex_proxy.setter  # 如果没有setter装饰，那么sex_proxy也是只读的，实例属性也无法覆盖，同property
    def sex_proxy(self, val):
        print("call set sex")
        self.__sex = val

    # ---------------------
    @my_static_method  # 相当于my_static_fun = my_static_method(my_static_fun)  就是非数据描述符
    def my_static_fun():
        print('my_static_fun')

    @my_class_method
    def my_class_fun(cls):
        print('my_class_fun')


# 主函数
if __name__ == "__main__":
    say("函数装饰器测试")
    '''
    日志输出开始
    函数装饰器测试
    结束日志输出
    '''
    t = test()  # 创建测试类的实例对象
    '''
    before __setattr__    
    after __setattr__
    before __setattr__
    after __setattr__
    before __setattr__
    after __setattr__
    '''
    print(str(t))  # 验证__str__内建函数
    '''
    start call __getattribute__
    start call __getattribute__
    start call __getattribute__
    name is test,age is 0,sex is man
    '''
    print(repr(t))  # 验证__repr__内建函数
    '''
    start call __getattribute__
    start call __getattribute__
    start call __getattribute__
    name is test,age is 0,sex is man
    '''
    t.fly()  # 验证类装饰器
    '''
    start call __getattribute__
    这是一个测试类
    '''
    t.my_static_fun()  # 验证自定义静态方法
    '''
    start call __getattribute__
    call myStaticObject __get__
    my_static_fun
    '''
    t.my_class_fun()  # 验证自定义类方法
    '''
    start call __getattribute__
    call myClassObject __get__
    my_class_fun
    '''
    # 以下为属性获取
    t.d1
    '''
    start call __getattribute__
    call des1.__get__
    '''
    t.d2
    '''
    start call __getattribute__
    call des2.__get__
    '''
    t.d3()
    '''
    start call __getattribute__
    i am a function
    '''
    t.name_proxy
    '''
    start call __getattribute__
    call test.get_name
    start call __getattribute__
    '''
    t.age_proxy
    '''
    start call __getattribute__
    call test.get_age
    start call __getattribute__
    '''
    t.sex_proxy
    '''
    start call __getattribute__
    call get sex
    start call __getattribute__
    '''
    t.xyz  # 测试访问不存在的属性，会调用__getattr__
    '''
    start call __getattribute__
    start call __getattr__
    '''
    # 测试属性写
    t.d1 = 3  # 由于类属性d1是非数据描述符，因此这里将动态产生实例属性d1
    '''
    before __setattr__
    after __setattr__
    '''
    t.d1  # 由于实例属性的优先级比非数据描述符优先级高，因此此处访问的是实例属性
    '''
    start call __getattribute__
    '''
    t.d2 = 'modefied'
    '''
    before __setattr__
    call des2.__set__,val is modefied
    after __setattr__
    '''
    t.d2
    '''
    start call __getattribute__
    call des2.__get__
    '''
    t.d3 = 'not a function'
    '''
    before __setattr__
    after __setattr__
    '''
    t.d3  # 因为函数是非数据描述符，因此被实例属性覆盖
    '''
    start call __getattribute__
    '''
    t.name_proxy = 'modified'
    '''
    before __setattr__
    call test.set_name
    before __setattr__
    after __setattr__
    after __setattr__
    '''
    t.sex_proxy = 'women'
    '''
    before __setattr__
    call set sex
    before __setattr__
    after __setattr__
    after __setattr__
    '''
    t.age_proxy = 3  # age_proxy是只读的
    '''
    before __setattr__
    Traceback (most recent call last):
      File "contest.py", line 191, in <module>
       t.age_proxy = 3
      File "contest.py", line 121, in __setattr__
       super(test, self).__setattr__(name, value)
    AttributeError: can't set attribute
    '''
