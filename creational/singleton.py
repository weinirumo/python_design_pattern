# -*- coding: utf-8 -*-

class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance


if __name__ == "__main__":
    a = Singleton()
    a.hw = 'hello world'

    b = Singleton()
    print(b.hw)  # hello world

    print(hex(id(a)))  # 0x1033a9748
    print(hex(id(b)))  # 0x1033a9748

