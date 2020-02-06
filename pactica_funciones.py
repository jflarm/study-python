#!/usr/bin/python3.7
def newfunc(a,b):
    def otherfunc(c,d):
        return c * d
    print(otherfunc(a,b))
    return a + b

    

print(newfunc(3,9))

