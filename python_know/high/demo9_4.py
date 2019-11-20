import time


def timer(label="", trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elasped = time.clock() - start
            self.alltime += elasped
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elasped, self.alltime)
                print(format % values)
            return result

    return Timer


@timer
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))


@timer(label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return map((lambda x: x * 2), range(N))


for func in (listcomp, mapcall):
    print('')
    result = func(5)
    func(50000)
    func(500000)
    func(1000000)
    print(result)
    print('allTime = %s' % func.alltime)  # Total time for all calls
print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
