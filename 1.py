class Truck:
    def set__color(self,color):
        self.__color=color
    
    def get__color(self):
        return self.__color

obj=Truck()
obj.set__color("White")
print(obj.get__color())