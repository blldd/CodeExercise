# -*- coding:UTF-8 -*-

import threading

"""
单例模式是指，该对象创建后，在其生命周期内内存中始终只有一个对象， 如果被再次调用时，还是返回该对象。 
这样做的好处是，可以节约内存，缺点是不可以根据不同的应用场景创建不同的对象。

多线程环境下，由于单例模式总是会去判断 实例是否被创建，但是多个线程有可能会拿到相同的结果，这样就无法实现单例模式了.
因此遇到多线程的环境时，需要加锁。

"""

def synchronized(func):

    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


class Singleton(object):
    """
    单例模式
    加了锁之后，每个线程判断 if cls.instance is None 这里就变成了线程安全。因此可以实现多线程环境下，始终只有一个实例
    """
    instance = None

    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


#
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance