import inspect


def gen():
    yield 2
    yield 3


g = gen()
print(inspect.getgeneratorstate(g))

print(next(g))
print(inspect.getgeneratorstate(g))


print(next(g))
print(inspect.getgeneratorstate(g))

try:
    next(g)
except StopIteration:
    pass

print(inspect.getgeneratorstate(g))
