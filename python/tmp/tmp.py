from flask import Flask

a = {1, 2, 3}

b = list(map(lambda x: x ** 2, a))
print(b)


# for i in b:
#     print(i)


def testarg(*args, operator):
    total = 1
    if operator == "*":
        for arg in args:
            total = total * arg
    return total


aa = testarg(2, 2, 3, operator="*")
print(aa)


# def named(name, age):
#     print(name, age)

def named(**args):
    print(args)


details = {"name": "Bob", "age": 25}
named(**details)
