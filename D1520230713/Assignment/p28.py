keychains=0
cost_keychain=10
ship_per_key=5
addition_ship=1
sales_tax=8.25

def add_keychains(keychains):
    num=int(input("How many keychains to add?"))
    keychains+=num
    print(f"Now you have {keychains}")


def rem_keychains(keychains):
    num=int(input("How many keychains to remove?"))
    keychains-=num
    return(f"Now you have {keychains} keychains")

def view_order(keychains,cost_keychain,ship_per_keys,addition_ship,sales_tax):
    total=keychains*cost_keychain
    shipping=ship_per_keys+(keychains*addition_ship)
    sub=total+shipping
    sub_tax=sub*(sales_tax/100)
    final=total+shipping+sub_tax

    print(f"Now you have {keychains}")
    print(f"Total cost of keychains is {total}")
    print(f"Shipping charge of order is {shipping}")
    print(f"subtotal is {sub}")
    print(f"subtotal with tax is {sub_tax}")
    print(f"The final cost is {final}")

def checkout(keychains,cost_keychain,ship_per_keys,addition_ship,sales_tax):
    name=input("Enter your name:")
    view_order(keychains,cost_keychain,ship_per_keys,addition_ship,sales_tax)
    print(f"Thanks for ordering {name}")
    print(f"Now you have {keychains} keychains")



while True:
    print("1.Add keychain to order")
    print("2.Remove keychain from order")
    print("3.View Current Order")
    print("4.Checkout")
    a=int(input("Please enter your choice:"))
    if a==1:
        add_keychains(num_keychains)
    elif a==2:
        rem_keychains(keychains)
    elif a==3:
        view_order(keychains,cost_keychain,ship_per_key,addition_ship,sales_tax)
    elif a==4:
        checkout(keychains,cost_keychain,ship_per_key,addition_ship,sales_tax)
        break
    else:
        print("Invalid choice")


