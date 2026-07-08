class Rect:
    greet="Hello I am Rect class" # class attribute

    count=0 # class attribute
    def __init__(self,len=1,bre=1): # constructor
        self.l=len  # l and b is here instance attribute
        self.b=bre
        Rect.count+=1 # incrementing count for each object creation
        self.id=Rect.count # assigning unique id to each object
        self._extra="1" 
    def display(self):  # method
        print(f"Dimension of Rect{self.id}: {self.l}x{self.b}")
        
    def area(self): 
        return self.l*self.b
    def parimeter(self):
        return 2*(self.l+self.b)
    
