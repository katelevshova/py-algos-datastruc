print("------------------")
x = {'foo': 'bar'}
y={'baz':x}
z = y['baz']['foo']
print(z)

print("------------------")
import math
x = math.fsum([x*x for x in [1,2,3]])
print(x)

