# Automatic Garbage Collection

import gc

class myclass:
    
    def __del__(self):
        print("deleted")
        
obj = myclass
del obj
gc.collect()

#Garbage collection--Python automatically removes unused objects to free memory using garbage collection.