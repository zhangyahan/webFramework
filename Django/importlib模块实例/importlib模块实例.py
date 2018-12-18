from xx import oo


print(oo.NAME)

p = oo.Person('张雅涵')
p.dream()


import importlib

model = importlib.import_module('xx.oo')
s = hasattr(model, 'Person')
print(s)
print(model.Person)