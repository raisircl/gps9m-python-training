class Rect:
    greet="Hello I am Rect class" # class attribute

    count=0 # class attribute
    def __init__(self,len=1,bre=1): # constructor
        self.__l=len  # l and b is here instance attribute
        self.__b=bre
        Rect.count+=1 # incrementing count for each object creation
        self.id=Rect.count # assigning unique id to each object
        self._extra="1" 
    @property
    def Length(self):
        return self.__l
    @Length.setter
    def Length(self,value):
        self.__l=value
    @property
    def Breadth(self):
        return self.__b
    @Breadth.setter
    def Breadth(self,value):
        self.__b=value

    def display(self):  # method
        print(f"Dimension of Rect{self.id}: {self.__l}x{self.__b}")
        
    def area(self): 
        return self.__l*self.__b
    def parimeter(self):
        return 2*(self.__l+self.__b)
    
    @classmethod
    def get_count(cls):
        return cls.count
    def __str__(self):
        return f"Rect{self.id} dimension: {self.__l}x{self.__b}"
    def __add__(self,r2):
        temp=Rect()
        temp.Length=self.Length+r2.Length
        temp.Breadth=self.Breadth+r2.Breadth
        return temp