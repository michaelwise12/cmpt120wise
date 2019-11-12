# RobotShop.py
# Author: Michael Wise
# CMPT 120: Lab #8 - Working with Objects

class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def inStock(self, count):
        if count <= self.quantity:
            return True
        else:
            return False

    def totalCost(self, count):
        return self.price * count

    def purchase(self, count):
        self.quantity -= count
        
def printStock(prod):
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(prod)):
        if prod[i].quantity > 0:
            print(str(i)+")",prod[i].name, "$", prod[i].price)
    print()
    
def main():
    cash = float(input("How much money do you have? $"))

    prod = [Product("Ultrasonic range finder",2.50,4),
            Product("Servo motor", 14.99, 10),
            Product("Servo controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser range finder", 149.99, 2),
            Product("Lithium polymer battery", 8.99, 8)]

    while cash > 0:
        printStock(prod)
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        
        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        count = int(vals[1])
        
        if prod[prodId].inStock(count):
            if cash >= prod[prodId].totalCost(count):
                prod[prodId].purchase(count)
                cash -= prod[prodId].totalCost(count)
                print("You purchased", count, prod[prodId].name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", prod[prodId].name)
            
main()
