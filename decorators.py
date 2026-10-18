def add(func):
    def extraline():
        print("Function Started")
        func()

    return extraline


@add
def hello():
    print("Hello!")


hello()
