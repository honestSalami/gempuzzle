#!  /usr/bin/python3


ava = list(range(10))

def catchExceptions(*exceptions):
    def _catch(fun, *args, **kws):
        try:
            rtn = fun(*args, **kws)
        except ().extend(*exceptions) as e:
            print("sorry, no dice\n")
        return rtn
    return _catch

def insist():
    """Decorator. Run fun until it does not
    return one of the exceptions.
    """
    def decorator(fun):
        def wrapper(*args, **kws):
            while True:
                try:
                    return fun(*args, **kws)
                # bad, hard code
                except IndexError:
                    print("index")
                except ValueError:
                    print("value")
        return wrapper
    return decorator

# the name askAndGet wouldn't make sense
# without the insist decorator.
@insist()
def askAndGet(lst):
    print(lst)
    index = int(input("just a test: "))
    print(lst[index])

askAndGet(ava)
