
def uuid_gen(idx=1):
    while True:
        idx = yield
        idx += 1


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


@coroutine
def filter_first_list(target):
    while True:
        try:
            list_yielded = yield
            filtered_element = list_yielded[1:]
            target.send(filtered_element)
        except StopIteration as e:
            print('Filter: I am done')
            return e.value


@coroutine
def double_first_list(target):
    while True:
        try:
            list_yielded = yield
            first_element = list_yielded[0]
            list_yielded = [first_element * 2, *list_yielded[1:]]
            target.send(list_yielded)
        except StopIteration as e:
            print('Double: I am done')
            return e.value


@coroutine
def square_list():
    list_yielded = yield
    new_list = [a ** 2 for a in list_yielded]
    return new_list


def get_data(coro, iterable):
    try:
        coro.send(iterable)
    except StopIteration as e:
        print(e.value)


get_data(filter_first_list(double_first_list(square_list())), [2, 3, 4, 5, 6])

