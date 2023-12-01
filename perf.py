import time

def clock(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        duration = te - ts

        print(f"func:{f.__name__} took: {duration:2.12f} sec")
        return result

    return timed