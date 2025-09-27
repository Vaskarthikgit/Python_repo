class menu:
    def __init__(self, name, price):
        self.name=name
        self.price=price

menu_lst=[
    menu("Coffee",50),
    menu("Tea",40),
    menu("Juice",70),
    menu("Burger",100)
]

class order:
    def __init__(self):
        self.items=[]

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added in order \n")

    def total(self):
        return sum(item.price for item in self.items)

order = order()

while True:
    print("Menu:")

    for i, item in enumerate(menu_lst,1):
        print( f"{i}. {item.name} ₹{item.price}" )

    print("5. Place the order")
    print("6. Exit")

    option=input("Enter your option to add item to cart:")

    if option == '5':
        print("Order is placed!")
        print(f"Total price: {order.total()}")
        break
    elif option == '6':
        print("Exit from order!")
        break
    else:
        order.add_item(menu_lst[int(option)-1])