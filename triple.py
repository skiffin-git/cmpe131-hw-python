def tripler(fnc):
    def func():
        fnc()
        fnc()
        fnc()
    return func
