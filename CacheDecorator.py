'''Targil 6'''

class memorize(dict):

    """ Constructor """
    def __init__(self, func_name):
        self.func_name = func_name

    """ Return result of function call if cached"""
    def __call__(self, *args):
        return self[args]

    """ Return result of function call and cache the result """
    def __missing__(self, key):  
        result = self[key] = self.func_name(*key)
        return result


@memorize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def main():
    print("fibo: ", fib(10))
    print("Cached Results: ", fib)  # all factorials from 1 to 5 are cached
    print("fibo: ", fib(5))
    print("Cached Results: ", fib)


if __name__ == "__main__":
    main()

