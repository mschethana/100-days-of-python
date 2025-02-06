data_coffee={
            "expresso":{
                "water":50,"coffee":18,"milk":0,"price_dollar":1.50
                },
             "latte":{
                 "water":200,"coffee":24,"milk":150,"price_dollar":2.50
                },
             "cappuccino":{
                 "water":250,"coffee":24,"milk":100,"price_dollar":3.00
                }
             }
resources={
            "total_water_remaining":300,
            "total_milk_remaining":200,
            "total_coffee_remaining":100
           }
coint_types_dollar={"penny":0.01,"dime":0.10,"nickel":0.05,"quarter":0.25}
def coin_input():
    q=int(input("How many quarters have you inserted? "))
    n=int(input("How many nickel have you inserted? "))
    d=int(input("How many dime have you inserted? "))
    p=int(input("How many penny have you inserted? "))
    total_inserted=float((q*coint_types_dollar["quarter"])+(n*coint_types_dollar["nickel"])+(d*coint_types_dollar["dime"])+(p*coint_types_dollar["penny"]))
    return total_inserted
def change(total,cash):
    balance=cash-total
    return balance
def resource_balance(water,milk,coffee):
    resources["total_water_remaining"]-=water
    resources["total_milk_remaining"]-=milk
    resources["total_coffee_remaining"]-=coffee
    return resources
def check_resource(flavor):
    is_water=resources["total_water_remaining"]-data_coffee[flavor]["water"]
    is_coffee=resources["total_coffee_remaining"]-data_coffee[flavor]["coffee"]
    is_milk=resources["total_milk_remaining"]-data_coffee[flavor]["milk"]
    if is_water<0:
        print("Sorry! There is not enough water - Please order something else")
        return False
    elif is_coffee<0:
        print("Sorry! There is not enough coffee - Please order something else")
        return False
    elif is_milk<0:
        print("Sorry! There is not enough milk - Please order something else")
        return False
    else:
        return True

revenue=float(0)
def output(insert):
    if insert=='report':
        print(f"Water: {resources['total_water_remaining']} ml\nCoffee: {resources['total_coffee_remaining']} g\nMilk: {resources['total_milk_remaining']}ml\nMoney: ${revenue}\n")
    elif insert=='expresso'or insert=='latte' or insert=='cappuccino':
        if check_resource(insert)==True:
            total=data_coffee[insert]["price_dollar"]
            print(f"Total to be paid: ${total}")
            print("Please insert coins\n")
            input_money=coin_input()
            print(f"Total amount inserted is ${input_money}")
            balance=change(total,input_money)
            if balance<0:
                print("Amount inserted is not enough! Money has been refunded")
                return
            print(f"Your balance is: ${balance}")
            print(f"Here is your {insert}! Have a great day!! :)")
            resource_balance(data_coffee[insert]["water"],data_coffee[insert]["milk"],data_coffee[insert]["coffee"])
            return float(total)
        else:
            return
want_coffee=True
while want_coffee:
    customer_input=input("What would you like? (Expresso/Latte/Cappuccino): ").lower()
    if customer_input=='expresso'or customer_input=='latte' or customer_input=='cappuccino':
        add=output(customer_input)
        if isinstance(add,float):
            revenue=revenue+add
    elif customer_input=='off':
        want_coffee=False
    else:
        output(customer_input)
    
    


      
