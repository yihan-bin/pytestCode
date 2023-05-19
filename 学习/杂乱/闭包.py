def funout(num1):
    def funin(num2):
        # nonlocal  num1
        # num1+=300
        return num1+num2
    return funin


f=funout(100)
x=10
x *= 2 if isinstance(x,dict) == 1 else 1
print(type(f))
print(f(200))
assert False, 'either --cfg or --weights must be specified'