from abc import ABC,abstractmethod
from random import randint
import sortedcontainers as sc
class Order(ABC):
    def __init__(self,Price,Quantity):
        self.Price = Price
        self.Quantity = Quantity

    @property
    def elements(self):
        return [self.Price,self.Quantity]


    def __tuple__(self):
        return self.Price,self.Quantity

    def __list__(self):
        return [self.Price, self.Quantity]

    def __repr__(self):
        return f"{self.__class__.__name__}(Price= {self.Price } , Quantity= {self.Quantity})"

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    @abstractmethod
    def __gt__(self,Order):
       pass

    @classmethod
    def generate(cls,Price_min,Price_max,Quantity_max,N):
        for i in range(N):
          yield cls(randint(Price_min, Price_max), randint(0, Quantity_max))

class Ask_Order(Order):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def __gt__(self,Ask_Order):
       return self.Price > Ask_Order.Price


class Bid_Order(Order):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def __gt__(self,Bid_Order):
       return self.Price < Bid_Order.Price


if __name__ == '__main__':
    ordre1 = Ask_Order(10,1)
    ordre2 = Ask_Order(11, 1)
    print(ordre2)
    order_set = { ordre1 , ordre2 }
    print(order_set)

    ordre3 = Bid_Order(10,1)
    ordre4 = Bid_Order(11, 1)

    order_set = { ordre4 , ordre3 }
    print(order_set)

    #print(Ask_Order.generate(Price = 100, Quantity = 10))
    print(sc.SortedList(Bid_Order.generate(2,3,100)))





