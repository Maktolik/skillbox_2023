def singleton(cls):
    def wrapped(*args, **kwargs):
        if cls.tmp is None:
            instance = cls(*args, **kwargs)
            cls.tmp = instance
            return instance
        return cls.tmp

    cls.tmp = None
    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

