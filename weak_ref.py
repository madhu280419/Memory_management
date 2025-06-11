#Weak References (weakref module)

import weakref

class data:
    def __init__ (self,name):
        self.name = name
        
d = data("Jaunty")
weak_d = weakref.ref(d)

print(weak_d().name)

del d
print(weak_d())