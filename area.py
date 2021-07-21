def decorator(func):
    def decorated(a,b):
        if a<0 or b<0:
            print('length error')
        else:
            func(a,b)
    return decorated


@decorator
def triangle(a,b):
    print("삼각형의 넓이:{}".format(a*b/2))
@decorator
def angular(a,b):
    print("사각형의 넓이:{}".format(a*b))

triangle(10,10)
triangle(10,-10)
triangle(-10,10)
triangle(-10,-10)

angular(10,10)
angular(10,-10)
angular(-10,10)
angular(-10,-10)