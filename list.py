#!/user/bin/python

a = [1,2,7,"str",1.76]

for i in range(len(a)):
    print(f"{i} : {a[i]*2}")

b = a
a[0] = 100
print(a,b)

def foo(a:int, b:list=[])
    b.append(a)
    return b

print(foo(1))
print(foo(2),[]))
print(foo(3))

