keychains=0
shipping_cost=5
ship_per_key=1
key_cost=10
sales_tax=8.25


def add_keychains(keychains):
    num=int(input("How many keychains to add?"))
    keychains+=num
    return keychains

def rem_keychains(keychains):
    num=int(input("How many keychains to remove?"))
    keychains-=num
    return keychains

def view():
    keychains=num_keychains(keychains)


while True:
    print("Add keychains")
    print("Remove Keychains")
    print("View Order")
    print("Checkout")
    a=int(input("Enter your choice:"))
    if a==1:
        add_keychains(keychains)
    if a==2:
        rem_keychains(keychains)
    if a==3:




