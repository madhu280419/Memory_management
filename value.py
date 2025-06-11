import gc

class example:
    
    def __init__(self,value):
        self.value = value
        
obj = example(204)
obj1 = obj  

del obj1
gc.collect()   