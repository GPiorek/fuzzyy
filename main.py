import simpful

def triangle(x,a,b,c):
    if x < a or x > c:
        return 0.0
    if x == b:
        return 1.0
    elif x <= b:
        return (x-a)/(b-a)
    elif x>=b:
        return (x-c)/(b-c)


