print("Ye Olde Keychain Shoppe")
print("\n")
def key():
    print("1.Add keychain to order")
    print("2.Remove keychain from order")
    print("3.View Current Order")
    print("4.Checkout")
    a=int(input("Please enter your choice:"))
    if a==1:
        add_key()
    if a==2:
        rem_key()
    if a==3:
        view_order()
    if a==4:
        checkout()
def add_key():
    print("ADD KEYCHAIN")
    key()
def rem_key():
    print("REMOVE KEYCHAIN")
    key()
def view_order():
    print("View order")
    key()
def checkout():
    print("CHECKOUT")
key()