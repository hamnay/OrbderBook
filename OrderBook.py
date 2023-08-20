import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import sortedcontainers as sc
from Order import Bid_Order,Ask_Order


class OrbderBook:
    def __init__(self):
        self.Bid = sc.SortedList()
        self.Ask = sc.SortedList()
    def add_to_Bid(self, Order):
        if isinstance(Order,Bid_Order):
           self.Bid.add(Order)
        elif isinstance(Order,(sc.SortedList,list)):
           self.Bid+=Order


    def add_to_Ask(self,Order):
        if isinstance(Order, Ask_Order):
           self.Ask.add(Order)
        elif isinstance(Order, (sc.SortedList,list)):
           self.Ask+= Order

    def plot(self):
        BidPrices,BidQuantities = zip(*reversed(self.Bid))
        Bidlength = len(BidPrices)
        plt.bar( x = range(-Bidlength,0,1), height = BidQuantities , color = 'b' )
        #plt.xticks(range(Bidlength), BidPrices)

        AskPrices, AskQuantities = zip(*self.Ask)
        Asklength = len(AskPrices)
        plt.bar( x = range(Asklength), height = AskQuantities , color = 'r' )
        plt.xticks( range(-Bidlength,Asklength,1), BidPrices + AskPrices)

        plt.show()

    @property
    def in_equilibrum(self):
        return self.Bid[0] < self.Ask[0]






if __name__ == "__main__" :
    OB = OrbderBook()
    Bid_Orders = sc.SortedList(Bid_Order.generate(Price_min = 0, Price_max = 100 , Quantity_max = 20 ,N = 30 ))
    OB.add_to_Bid(Bid_Orders)
    print(OB.Bid)
    Ask_Orders = sc.SortedList(Ask_Order.generate(Price_min = 101, Price_max = 200 , Quantity_max = 20 ,N = 30 ))
    OB.add_to_Ask(Ask_Orders)
    print(OB.Ask)
    OB.plot()
    print(OB.in_equilibrum)