class product:

    def __init__(self, pid, name, price):
        self.pid=pid
        self.name=name
        self.price=price

    def display(self):
        print(f"ID: {self.pid}")
        print(f"NAME: {self.name}")
        print(f"PRICE: {self.price}")

class Cart:

    def __init__(self):
        self.__cart=[]

    def add_product(self, product):
        self.__cart.append(product)
        print(f"{product.name} added to cart")

    def remove_product(self, pid):
        for product in self.__cart:
         if product.pid==pid:
             self.__cart.remove(product)
             print(f"{product.name} removed from the cart")
             return
        print("Product not found")
         
    def view_cart(self):
        if len(self.__cart)==0:
            print("Cart is empty")
            print("____Shopping Cart____")
            
        for product in self.__cart:
            product.display()
            print("-------------------------")

p1=product(101, "Laptop", 60000)
p2=product(102, "Mouse", 500)
p3=product(103, "Keyboard", 4000)
p4=product(104, "Bluetooth", 3000)

cart=Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

print("\n____cart after adding products____")
cart.view_cart()

cart.remove_product(102)

print("\n____cart after removing product____")
cart.view_cart()

cart.remove_product(201)