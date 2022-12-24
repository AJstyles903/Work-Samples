import phone

ipad_type=["ipad pro 11","ipad pro 12","ipad mini"]
ipad_price = [295,325,254]
sales = []


def sales_print():
    for i in range(len(sales)):
        sales[i].sale_print()


def buy(choice):
    type=ipad_type[choice-1]
    price=ipad_price[choice-1]
    name = input("Enter Your Name: ")
    number = int(input("Enter Your Number: "))
    new_sale = phone.sale(type, price, name, number)
    sales.append(new_sale)


for i in range(10000):
    print("1.Sell ipad")
    print("2.Print All Sales")
    print("3.Exit")
    result = int(input("Choose: "))
    if result == 1:
        print("Which ipad do you want:")
        for i in range(len(ipad_type)):
            print(f"{i+1}.{ipad_type[i]}")
        choice = int(input("Choose: "))
        print("Price =",ipad_price[choice-1],"Thank you")
        if choice==1 :
            buy(choice)
        elif choice ==2:
            buy(choice)
        elif choice ==3:
            buy(choice)
        else:
            print("Please Choose Valid Number.")
    elif result == 2:
        sales_print()
    elif result == 3:
        break
    else:
        print("Please Choose Valid Number.")
