print("Ye Olde Keychain Shoppe")
print("\n")
b=0
def key(b):
    
    print("1.Add keychain to order")
    print("2.Remove keychain from order")
    print("3.View Current Order")
    print("4.Checkout")
    a=int(input("Please enter your choice:"))
    if a==1:
        add_key(b)
    if a==2:
        rem_key(b)
    if a==3:
        view_order(b)
    if a==4:
        checkout(b)
        print("\n")
def add_key(b):
    add=int(input(f"You have {b} keychains. How many to add?"))
    print(f"You now have {add} keychains")
    b+=add
    key(b)
    print("\n")
def rem_key(b):
    rem=int(input(f"You have {b} keychains. How many to remove?"))
    b-=rem
    print(f"You now have {b} keychains")
    key(b)
    print("\n")
def view_order(b):
    print(f"You now have {b} keychains")
    print("Keychains cost $10 each")
    ch=b*10
    print("Total cost:",ch)
    key(b)
    print("\n")
def checkout(b):
    print("CHECKOUT")
    name=input("What is your name?")
    print(f"You have {b} keychains")
    print("Keychains cost $10 each")
    ch=b*10
    print("Total cost:",ch)
    print(f"Thanks for your order,{name}!")
key(b)
