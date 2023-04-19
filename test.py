a = ''

def test():
    global a
    b = '3'
    a = b

test()
print(a)